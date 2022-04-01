## Product

| Database Key 	| Type      	| Relationship 	|
|--------------	|-----------	|--------------	|
| category     	|           	| Foreign Key  	|
| name         	| Char(200) 	|              	|
| description  	| Char(200) 	|              	|
| price        	| Float     	|              	|
| size        	| Float     	|              	|
| rating       	| Float     	|              	|
| img          	| Image     	|              	|
| img_url      	| Url       	|              	|
| added_date    | Date       	|              	|



## Category

| Database Key 	| Type       	| Relationship 	|
|--------------	|------------	|--------------	|
| name         	| Char (200) 	|              	|

## Order

| Database Key   	| Type  	| Relationship 	|
|----------------	|-------	|--------------	|
| order_number   	| Int   	| Primary Key  	|
| user           	|       	| Foreign Key  	|
| order_date     	| Date  	|              	|
| name           	| Char  	|              	|
| email          	| Char  	|              	|
| phone_number   	| Char  	|              	|
| country        	| Char  	|              	|
| city           	| Char  	|              	|
| postal_code    	| Char  	|              	|
| street_address 	| Char  	|              	|
| co             	| Char  	|              	|
| delivery_cost  	| Float 	|              	|
| order_total    	| Float 	|              	|
| grand_total    	| Float 	|              	|


## Order Line Item

| Database Key 	| Type 	| Relationship 	|
|--------------	|------	|--------------	|
| order        	|      	| Foreign Key  	|
| product      	|      	| Foreign Key  	|
| quantity     	| Int  	|              	|
| price        	| Char 	|              	|
