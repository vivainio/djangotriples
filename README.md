Backend for dumping JSON-LD like annotations of objects, and query them.

This can be used e.g. for rating/commenting system. POSTing this kind of JSON object

```json
{
	'@id' : "com.myapp",
	'rating' : "5.5",
	'comment' : 'Rubbish!'
}
```

 ...to /api/v1/put/, creates (subject, predicate, object) pairs:

```python
("com.myapp", "rating", "5.5"),
("com.myapp", "comment", "Rubbish!")
```


