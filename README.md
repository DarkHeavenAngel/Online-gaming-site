Online gaming site

I would like to have a website where visitors can browse through a catalog of games. The main page should feature a list of games, with a search option so that users can easily find titles by name, author, publisher or genre. I would also like to provide filters and sorting options, for example: cheapest games first, most expensive first, most popular, or by genre.

Each game should have its own dedicated page with full details about it. There should also be a section with authors — when a visitor clicks on an author, they should see all the games created by that person. The same applies to publishers: clicking on a publisher should show all the games they have released.

Visitors should be able to create an account and sign in. Once logged in, users will have their own profile page. In the profile, they should be able to update their personal details and review their purchase history. Registered users should also be able to add games to their shopping basket. When they decide to purchase, they can simply press a “Buy” button to place an order quickly (no extra steps like payment forms are required for now). Additionally, I would like registered users to be able to add their own games to the catalog, as well as edit or delete them later if needed.

Finally, the website should include an “About Us” page with contact details and basic information about delivery and returns.

----------------------------------------------------------------------------------------------------------------------------------

Endponts\
for games

Endpoint | Usage | Request method | Request body/parameters | Response status | Response body |
--- | --- | --- | --- |--- |--- |
/games | To get a list of games | GET | search, sort, limit, offset | 200 OK | ``` [{"id": 1, ``` <br/> ``` "title": Dying Light}] ``` <br/> ``` [{"genre": RPG, ``` <br/> ``` "price": 349}] ```| 
/games/{id} | To get game details | GET | - | 200 OK | ``` [{"id": 1, ``` <br/> ``` "title": Dying Light}] ``` <br/> ``` [{"genre": RPG, ``` <br/> ``` [{"description": action game..., ``` <br/> ``` "price": 349}] ```| 
/games | To add a game | POST | ``` [{"id": next id, ``` <br/> ``` "title": new name}] ``` <br/> ``` [{"genre": RPG, ``` <br/> ``` [{"description": action game..., ``` <br/> ``` "price": new price}] ``` <br/> ``` "author-id": new id}] ``` <br/> ``` "publisher-id": new id}] ``` | 201 Created | A game added| 
/games/{id} | To update game details | PUT | ``` {"price: different price"} ``` | 200 OK | The game updated| 
/games/{id} | To delete game | DELETE | - | 204 No Content | -| 
