## Ports
Django: <i><b>8000</b></i> <br>
PostgreSQL: <i><b>5432</b></i>


## Authorization

<b>Header</b> <br>
Authorization: Baerer {JWT_ACCESS_TOKEN}

## Methods

- POST /api/login<br>
    Request:
    {
      "email": string,
      "password": string
    }<br>
    Response:
    {
      "user": object,
      "token": string
    }


- POST /api/signup<br>
    Request: 
    {
      "email": string,
      "password": string
    }<br>
    Response:
    {
      "user": object,
      "token": string
    }


- *GET /api/profile<br>
    Response:
    {
        "user": object
    }
  

 <i>*Authorization required</i>


