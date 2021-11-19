# RestaurantBE



docker ps 
docker exec -it db bash
psql -Umarcos -W web-db





# **Functionality**

- ## **Client**
  - [ ] Schedule Reservation
  - [ ] Delivery
  - [ ] Take Away
  - [ ] Order Food From the Table
  - [ ] Points Reward
  - [ ] Split the Bill
  - [ ] Add Friends
  - [ ] Pay Bill Online
  - [ ] **View the Food Time**

- ## **Waiter**
  - [ ] A / B / M Order
  - [ ] Relate a Client to an Order
  - [ ] Open and Close Tables
  - [ ] Create Bill

- ## **Waiter**
  - [ ] CRUD Order
  - [ ] Relate a Client to an Order
  - [ ] Open and Close Tables
  - [ ] Close Order
  - Responsibles for beverages

- ## **Cashier**?????
  - [ ] "Process" Bill phisically

- ## **Receptionist**
  - [ ] Organize the Tables
  - [ ] Organize the Schedules
  - [ ] Open Table (with or without a Clinte User)

- ## **Chef/Su-Chef**
  - [ ] CRUD Menu
  - [ ] CRUD Dishes
  - [ ] CRUD Inventory (ingredients, dinks, etc)
  - [ ] Organize Dishes in Kitchen

- ## **Sushi Master**
  - [ ] Takes the Sushi Order
  - [ ] CRUD Sushi Section in Menu
  - [ ] CRUD Sushi Dishes








docker exec -it db bash
psql -Umarcos -h db -p 5432 -d web-db


insert into "user" VALUES (1,'marcos', 'adsasd', 'mail+dsa@host.sad', '2008-11-11', 'adasgdajsgdjasgdjas', '329329');