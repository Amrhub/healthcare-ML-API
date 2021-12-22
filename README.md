# healthcare-ML-API

## API Documentation

[API Documentation](https://healthcaregp.herokuapp.com/docs)

URL: https://healthcaregp.herokuapp.com/<br>
endpoint: "/data": <br>

## <b>_POST_<b> request:

```js
{
"name": string,
"device_id": string
}
```

## <b>_GET_<b> request:

receives:
array of objects `for example`:

```json
[
  {
    "name": "Nasseratic",
    "device_id": "1"
  },
  {
    "name": "Nasseratic",
    "device_id": "2"
  }
]
```
