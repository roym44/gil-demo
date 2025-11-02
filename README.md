# gil-demo
Demo code for "It’s not the GIL it’s the Skill" talk at TechGym 2025


### example-1
This example demonstrates a simple *CPU-bound* task (counting by incrementing a variable).

- This can be run **single/mt/pool** for **n** times.
- **mt** creates threads in the classic way, **pool** uses *ThreadPoolExecutor* (which will be used in next examples).
- Here we see significant improvement in **mt** comparing GIL to NOGIL.

```bash
python3.14 1-count.py mt 50
python3.14t 1-count.py mt 50
```

### example-2
This example demonstrates a simple *IO-bound* task (crawling URLs).
- This can be run **single/mt/async** for **n** times.
- Here we see the improvement from one to the next one, with GIL.

```bash
python3.14 2-crawler.py single
python3.14 2-crawler.py mt
python3.14 2-crawler.py async
```

### example-3
This example demonstrates a simple *CPU-bound* task (counting by incrementing a variable).

- This can be run **mt/mp** for **n** times.
- **mt** for multithreading, **mp** for multiprocessing.
- Here we see significant improvement in **mt** (NOGIL) compared to **mp** in terms of memory.

```bash
python3.14t 1-count.py mp 100
python3.14 1-count.py mt 100
python3.14t 1-count.py mt 100
```


