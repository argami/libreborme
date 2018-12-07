from django.core.management.base import BaseCommand
from django.utils import timezone

import logging
import time

from borme.models import Config
# from borme.parser.postgres import psql_update_documents
import borme.parser.importer

from libreborme.utils import get_git_revision_short_hash

from threading import Thread
#from queue import Queue
import asyncio

THREADS = 200


class ThreadConvertJSON(Thread):
    def __init__(self, queue):
        super(ThreadConvertJSON, self).__init__()
        self.queue = queue

    def run(self):
        while True:
            json_path = self.queue.get()
            try:
                borme.parser.importer.from_json_file(json_path)
            except Exception as e:
                print('ERROR: {} ({})'.format(os.path.basename(pdf_path), e))
            self.queue.task_done()

async def worker(queue):
    while True:
        json_path = queue.get_nowait()
        try:
            borme.parser.importer.from_json_file(json_path)
        except Exception as e:
            print('ERROR: {} ({})'.format(os.path.basename(pdf_path), e))
        finally:
            queue.task_done()

class Command(BaseCommand):
    help = 'Import BORME JSON file(s)'

    def add_arguments(self, parser):
        parser.add_argument('files', metavar='FILE', nargs='+', type=str)
    
    def handle(self, *args, **options):
        self.set_verbosity(int(options['verbosity']))

        loop = asyncio.get_event_loop()
        start_time = time.time()
        
        q = asyncio.Queue()
        tasks = []
        for i in range(THREADS):
            task = asyncio.ensure_future((worker(q)))
            tasks.append(task)
            #t = ThreadConvertJSON(q)
            #t.setDaemon(True)
            #t.start()

        for filename in options["files"]:
            q.put_nowait((filename)) 

        #q.join()

        loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
        loop.close()
 
        config = Config.objects.first()
        if config:
            config.last_modified = timezone.now()
        else:
            config = Config(last_modified=timezone.now())
        config.version = get_git_revision_short_hash()
        config.save()

        # Update Full Text Search
        # psql_update_documents()

        # Elapsed time
        elapsed_time = time.time() - start_time
        print('\nElapsed time: %.2f seconds' % elapsed_time)

    def set_verbosity(self, verbosity):
        #if verbosity == 0:
        borme.parser.importer.logger.setLevel(logging.ERROR)
        #elif verbosity == 1:  # default
        #    borme.parser.importer.logger.setLevel(logging.INFO)
        #elif verbosity == 2:
        #    borme.parser.importer.logger.setLevel(logging.INFO)
        #elif verbosity > 2:
        #    borme.parser.importer.logger.setLevel(logging.DEBUG)
        #    logging.getLogger().setLevel(logging.DEBUG)
