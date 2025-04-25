import practicuscore as prt

worker_config = prt.WorkerConfig(worker_size=worker_size, startup_script=startup_script)

print("Starting worker...")
worker = prt.create_worker(worker_config)

print("Terminating worker...")
worker.terminate()
