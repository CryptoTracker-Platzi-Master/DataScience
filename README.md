
# Criptotracker-algorithms
# DataScience
Challenge #5 of Platzi Master

In this proyect is a way for show algorithms used in the cryptotracker app
https://cryptotrackerapi.herokuapp.com

Here you can calculate compound interest and nominal interest
## Acknowledgements

- [@larispardo](https://github.com/larispardo)
## API Reference

#### calculate compound interest

```http
  Post /compound/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `compound` | `string` | **Required**. |

Json example:

	{
    "capital": 25,
    "interes":0.08,
    "time":15
	}
#### Calculate nominal interest

```http
  Post /nominal/
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `nominal` | `string` | **Required**. |

Json example:
    {
	"nominal": 0.08,
	"periods": 12
    }
## Authors

Backend

- [@miguelalf](https://github.com/miguelalf)
- [@Loaezo](https://github.com/Loaezo)
- [@cexperto](https://github.com/cexperto)

Fronted

- [@LeoRincon](https://github.com/LeoRincon)
- [@jtomasvc](https://github.com/jtomasvc)

## Deployment

To deploy this project:

clone this repo

Install python3+


```bash
run
py -m venv <name venv>
py install -r requirements.txt
py manage.py runserver  

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  
## Tech Stack

**Client:** JavaScript, React, SCSS, HTML 

**Server:** Python, Django, MySql, AWS