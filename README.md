# gil-demo
Demo code for "It’s not the GIL it’s the Skill" talk at TechGym 2025


### example-1
This example demonstrates a simple *CPU-bound* task (counting by incrementing a variable).

- This can be run **single/multi/pool** for **n** times.
- **multi** creates threads in the classic way, **pool** uses *ThreadPoolExecutor* (which will be used in next examples).
- Here we see significant improvement in **multi** comparing GIL to NOGIL.

```bash
python3.14 1-count.py multi 50
python3.14t 1-count.py multi 50
```

### example-2
This example demonstrates a simple *IO-bound* task (crawling URLs).
- This can be run **single/multi/async** for **n** times.
- Here we see the difference between all techniques with GIL.

```bash
python3.14 2-crawler.py single 50
python3.14 2-crawler.py multi 50
python3.14t 2-crawler.py async 50
```
