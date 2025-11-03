# gil-demo
Demo code for "It’s not the GIL it’s the Skill" talk at TechGym 2025

## Preparation
Install python3.14 including the free-threaded version, as explained [here](https://py-free-threading.github.io/installing-cpython/).

Next, install the requirements for both version:
```
python3.14 -m pip install -r requirements.txt
python3.14t -m pip install -r requirements.txt
```

## Examples

### example-1
This example demonstrates a simple *CPU-bound* task (counting by incrementing a variable).

- This can be run **single/mt/pool** for **n** times.
- **mt** creates threads in the classic way, **pool** uses *ThreadPoolExecutor* (which will be used in next examples).
- Here we see significant improvement in **mt** comparing GIL to NOGIL.

```bash
python3.14 1-count.py mt 30
python3.14t 1-count.py mt 30
```

### example-2
This example demonstrates a simple *IO-bound* task (crawling 3 URLs).
- This can be run **single/mt/async** for **n** times on **n** threads.
- Here we see the improvement from one to the next one, with GIL.

```bash
python3.14 2-crawler.py single
python3.14 2-crawler.py mt
python3.14 2-crawler.py async
```

### example-3
This example demonstrates the same simple *CPU-bound* task (counting by incrementing a variable).

- This can be run **mt/mp** for **t** times, using **n** threads/processes.
- **mt** for multithreading, **mp** for multiprocessing.
- Here we see significant improvement in **mt** (NOGIL) compared to **mp** in terms of memory.

```bash
python3.14t 3-count.py mp 80 200
python3.14 3-count.py mt 80 200
python3.14t 3-count.py mt 80 200
```

### example-4
This example demonstrates *CPU-bound* and *IO-bound* tasks using a simple web server.


- There is a sync version using **Flask** and an async one using **FastAPI**.
- To run a controlled experiment both server apps are run using [**Granian**](https://github.com/emmett-framework/granian).
- To run the client there are implementation for **sync**/**async** accordingly.
- Here we see 

Flask App:
```bash
python3.14 -m granian --interface wsgi --workers 1 servers.sync_flask:app --port 8001
python3.14 4-api.py sync cpu
python3.14 4-api.py sync io
```
FastAPI App:
```bash
python3.14 -m granian --interface asgi --loop asyncio --workers 1 servers.async_fastapi:app --port 8002
python3.14 4-api.py async cpu
python3.14 4-api.py async io
```




