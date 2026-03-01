# Tables

## restaurants

```
id | name | address | city | cuisine_type | is_active

- id is Primary Key
```

## customers

```
id | name | email | phone_number | city | registration_date

- id is Primary Key
```

## menu

```
id | restaurant_id | item_id

- id is Primary Key
- restaurant_id is Foreign Key referencing restaurants id
- item_id is Foreign Key referencing items id
```

## items

```
id | name | description | price | category

- id is Primary Key
```

## orders

```
id | restaurant_id | customer_id | status | date_time | delivery_address

- id is Primary Key
- restaurant_id is Foreign Key referencing restaurants id
- customer_id is Foreign Key referencing customers id
```

## rating

```
id | description | rating_number | restaurant_id | customer_id

- id is Primary Key
- restaurant_id is Foreign Key referencing restaurants id
- customer_id is Foreign Key referencing customers id
```

## orders_items

```
id | order_id | item_id | quantity

- id is Primary Key
- order_id is Foreign Key referencing orders id
- item_id is Foreign Key referencing items id
```
