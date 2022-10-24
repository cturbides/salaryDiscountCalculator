# salaryDiscountCalculator
Aplication for see the net salary (the base salary minus some legal retentions).

# Retentions
> Administradora de Fondo de Pensiones (AFP)
> Is equal to the 2.87% of the net salary, with a maximun set to 9,334.68$ DOP

> Seguro Familiar de Salud (SFS)
> Is equal to the 3.04% of the net salary, with a maximun to 4,943.80$ DOP

> Impuestos Sobre la Renta (ISR)
> Apply just for net salaries (monthly) over ~34,667$ DOP. To calculate it we must start talking about anual values.


Being A.S = Anual Salaries:
| A.S < 416,220.01$ DOP | 0$ (exent) |    
| -- | -- |
| 416,220.01 < A.S < 624,329.00| 15% of (A.S - 416,220.01) |
| 624,329.01 < A.S < 867,123.00 | 31,216 + 20% of (A.S - 624,329.01) |
| 867,123.01 < A.S | 79,776 + 25% of (A.S - 867,123.01) |

## Installation
```sh
pip install pipenv
pipenv install
```

## How to start it - locally
```sh
cd salaryDiscountCalculator
touch .env #Creating an enviroment file
```

Now, let's get our SECRET_KEY:
```sh
python3
```

```python
>>> import secrets
>>> secrets.token_url_safe(60)
'iHLs6uXOxZuMNvgFsYX_eOFWPq1x3p4hha3C9ApPIjtpmhU6x3ZVUyXUARO5xvyfTlQquVstLpQxBe0l'
```

Copy it into .env file like this:
```sh
iHLs6uXOxZuMNvgFsYX_eOFWPq1x3p4hha3C9ApPIjtpmhU6x3ZVUyXUARO5xvyfTlQquVstLpQxBe0l
```

And finally just execute it:
```sh
python3 manage runserver
```
