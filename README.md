# Juicestore Bot

Shoe checkout bot specifically made for https://juicestore.com/
Bot monitors site looking for a product with the desired keyword. Once the product is found, a text message is sent to the owner via twilio 
and the bot starts the automated checkout process from picking a size, to auto filling payment and shipping info and finally checking out

***although this is specifically for  juicestore, it provides insight on how to automate processes on another website***


## Getting Started
Surf the site and find a product you would like to test it out with. Replace self.keyword with your desired keyword.
Then of course fill in all of your credentials for each auto fill field.
### Prerequisites

You will  need to have python 3+ installed. 

Install selenium via pip -- pip install selenium

Install Twilio via pip -- pip install twilio

You will need to configure the account ID and token with your own Twilio credentials in the constructor of the Bot class

### CONFIGURATION
Make sure you enter your twilio details into your bot constructor and uncomment self.client. 
On line 60 you will uncomment the text message portion and replace "from" with your twilio number.
ADJUST YOUR MONITOR REFRESH RATE, line 73. 


In the monitor function you can replace the URL in the first line if you would like(only works on juicestore and will only buy shoes at the moment)

### Installing

Ensure you have all required libraries+ credentials and keywords and launch! 
## Deployment

Sit back and watch the bot display all products on the page and look for your product! No need to keep refreshing the site wasting your life

## Authors

Kevin Sasso
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

