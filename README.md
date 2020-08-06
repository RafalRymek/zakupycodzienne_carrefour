# Carrefour_shopping_script

## My first automation test script in python which help book delivery date and add products to basket

### Before your first run a test you should:

1. Create account on https://zakupycodzienne.carrefour.pl/
2. Create settings.py file where you need to put:

`USER_LOGIN = "your login"`  
`USER_PASSWORD = "your password"`    
`ZAKUPYCODZIENNE_URL = "https://zakupycodzienne.carrefour.pl/"`

You need to choose your products:  
`milk = "Mlekovita Mleko Polskie spożywcze 3,2% 1 l"`  
`yogurt = "Bakoma Jogurt Bio naturalny 140 g"`  
`cheese = "Sierpc Ser królewski 135 g"`

And create your shopping list:  
`shopping_list = [milk, yogurt, cheese, cottage_cheese]`