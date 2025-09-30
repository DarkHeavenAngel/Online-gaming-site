## Online Gaming Site

I would like to have a website where visitors can browse through a catalog of games. The main page should feature a list of games, with a search option so that users can easily find titles by name, author, publisher or genre. I would also like to provide filters and sorting options, for example: cheapest games first, most expensive first, most popular, or by genre.

Each game should have its own dedicated page with full details about it. There should also be a section with authors — when a visitor clicks on an author, they should see all the games created by that person. The same applies to publishers: clicking on a publisher should show all the games they have released.

Visitors should be able to create an account and sign in. Once logged in, users will have their own profile page. In the profile, they should be able to update their personal details and review their purchase history. Registered users should also be able to add games to their shopping basket. When they decide to purchase, they can simply press a “Buy” button to place an order quickly (no extra steps like payment forms are required for now). Additionally, I would like registered users to be able to add their own games to the catalog, as well as edit or delete them later if needed.

Finally, the website should include an “About Us” page with contact details and basic information about delivery and returns.

----------------------------------------------------------------------------------------------------------------------------------

## Endponts

Endpoint | Usage | Request method | Request body/parameters | Response status | Response body |
--- | --- | --- | --- |--- |--- |
**For Games** | --- | --- | --- |--- |--- |
/games | To get a list of games | GET | search, sort, limit, offset | 200 OK | ``` [{"id": 1, ``` <br/> ``` "title": Dying Light ``` <br/> ``` "genre": RPG, ``` <br/> ``` "price": 349}] ```| 
/games/{id} | To get game details | GET | - | 200 OK | ``` {"id": 1, ``` <br/> ``` "title": Dying Light ``` <br/> ``` "genre": RPG, ``` <br/> ``` "description": action game..., ``` <br/> ``` "price": 349} ```| 
/games | To add a game | POST | ``` {"title": Hollow Knight ``` <br/> ``` "genre": Indie, ``` <br/> ``` "description": action game..., ``` <br/> ``` "price": 169 ``` <br/> ``` "author-id": 2 ``` <br/> ``` "publisher-id": } ``` | 201 Created | A game added| 
/games/{id} | To update game details | PUT | ``` {"price: different price"} ``` | 200 OK | The game updated| 
/games/{id} | To delete game | DELETE | - | 204 No Content | -|
**For Authors** | --- | --- | --- |--- |--- |
/authors | To get a list of authors | GET | search, limit, offset | 200 OK | ``` [{"id": 1, ``` <br/> ``` "name": Team Cherry}] ``` | 
/authors/{id} | To get author's details | GET | - | 200 OK | ``` {"id": 1, ``` <br/> ``` "name": Team Cherry ``` <br\> ``` "games": [{"id":5,"title":"Left 4 Dead 2"}] } ```| 
/authors | To add an author | POST | ``` {"name": Valve, ``` <br/> ``` "bio": information} ``` | 201 Created | New author have been added| 
/authors/{id} | To update author's details | PUT |  ``` {"bio": updated} ``` | 200 OK | The author updaated| 
/authors/{id} | To delete author | DELETE | - | 204 No Content | -| 
**For publishers** | --- | --- | --- |--- |--- |
/publishers | To get a list of publishers | GET | search, limit, offset | 200 OK | ``` [{"id": 1, ``` <br/> ``` "name": Ubisoft}] ``` | 
/publishers/{id} | To get publisher's details | GET | - | 200 OK | ``` {"id": 1, ``` <br/> ``` "name": Ubisoft ``` <br\> ``` "games": [...] } ```| 
/publishers | To add an publishers | POST | ``` {"name": Ubisoft, ``` <br/> ``` "country": Spain} ``` | 201 Created | New publisher have been added| 
/publishers/{id} | To update publishers's details | PUT |  ``` {"country": Canada} ``` | 200 OK | The publisher updaated| 
/publishers/{id} | To delete publisher | DELETE | - | 204 No Content | -| 
**For Authorization and users** | --- | --- | --- |--- |--- |
/regist | To register new user | POST | ``` {"name": Maria, ``` <br/> ``` "email": ..., ```  <br/> ``` "password": ...} ``` | 201 Created | New user have been created| 
/login | To login an user | POST | ``` {"email": ..., ``` <br/> ``` "password": ...} ``` | 200 OK | ``` {"token: csrf-token"} ```| 
/userprof | To open user's profile | GET | - | 200 OK | ``` {"name": Maria, ``` <br/> ``` "email": ...} ``` | 
/userprof | To update profile | POST | ``` {"name": Masha} ``` | 200 OK | Updated profile| 
**For shopping** | --- | --- | --- |--- |--- |
/cart | To view the cart | GET | - | 200 OK | ``` [{"item-id": 1, ``` <br/> ``` "game-id": 2, ``` <br/> ``` "name": Hollow Knight, ``` <br/>  ``` "quantity": 1}] ```| 
/cart | To add a game in a cart | POST | ``` {"game-id": 2, ``` <br/> ``` "quantity": 1} ``` | 201 Created | An item have been added| 
/cart/{item-id} | Update quantity | PUT | ``` {"quantity": 2, ``` | 200 OK | Items updated | 
/cart/{item-id} | Delete item | DELETE | - | 204 No Content | - | 
**For orders** | --- | --- | --- |--- |--- |
/orders | To see order history | GET | - | 200 OK | ``` [{"id": 1, ``` <br/> ``` "total": 64, ``` <br/> ``` "status": delivered ```| 
/orders/{id} | To see history of the order | GET | - | 200 OK | ``` {"id": 1, ``` <br/> ``` "games": [{"id":5, "title":"Left 4 Dead 2"}] } ``` <br/> ``` "quantity": 1, ``` <br/>  ``` "total": 64} ```| 
/orders | Create new order | POST | - | 201 Created | Order created | 
**For Information about us** | --- | --- | --- |--- |--- |
/info | To see information about us | GET | - | 200 OK | ``` [{"contacts": ..., ``` <br/> ``` "delivery": ..., ``` <br/> ``` "return": ... ```| 

----------------------------------------------------------------------------------------------------------------------------------

![alt text](https://github.com/DarkHeavenAngel/Online-gaming-site/blob/Description-branch/base.png)
