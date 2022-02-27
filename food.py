from Item import Item


def get_food():
  names = [['Hamburger',4.50, "hamburger.jpg", 'Hamburger made with love out of premium Beef and flavoured full b'], 
              ['Fries', 1.50, "fries.png", ''], 
              ['Coffee', 1.50, "coffee.jpg", ''],
              ['Tea', 1.50, "tea.jpeg", ''],
              ['Pizza', 8.50, "pizza.jpeg", ''],
              ['Pasta', 8.50, "pasta.jpeg", ''],
              ['Sushi', 8.50, "sushi.jpeg", ''],
              ['Mountain Dew', 200, "mountaindew.jpeg", ''],
              ['Creme Brulee', 200, "cremebrulee.jpeg", '']]
  food_list = [Item(name=food[0], price = food[1], image = f'images/{food[2]}', description = food[3])  for food in names]
  return food_list












'''
  hamburger = Item(
    name="Hamburger",
    price=4.50,
    image="images/hamburger.jpg"
  )

  food_list.append(hamburger)

  fries = Item(
    name="Fries",
    price=1.50,
    image="images/fries.png"
  )

  food_list.append(fries)
  coffee = Item(
    name="Coffee",
    price=1.50,
    image="images/coffee.jpg"
  )
  food_list.append(coffee)
  tea = Item(
    name="Tea",
    price=1.00,
    image="images/tea.jpeg"
  )
  food_list.append(tea)
  pizza = Item(
    name="Pizza",
    price=8.00,
    image="images/pizza.jpeg"
  )
  food_list.append(pizza)
  pasta = Item(
    name="Pasta",
    price=8.00,
    image="images/pasta.jpeg"
  )
  food_list.append(pasta)
  sushi = Item(
    name="sushi",
    price=6.00,
    image="images/sushi.jpeg"
  )
  food_list.append(sushi)
  mountain_dew = Item(
    name="Mountain Dew",
    price=10.00,
    image="images/mountaindew.jpeg"
  )
  food_list.append(mountain_dew)
 '''



  
  