import scrapy

class YellowpagecitySpider(scrapy.Spider):
    name = 'yellowpagecity'; 
    start_urls = ['http://www.yellowpagecity.com/US/NY/New+York/Health+Clubs/']; 
    

    def parse(self, response):
        # Access the container that contains the information of the business. 
        listings = response.xpath('//a[@class="listing-wrap"]'); 
        
        for listing in listings: 
            # get the name, address and phone number of the business. 
            name = listing.xpath('.//span[@id="name"]/text()').get(); 
            address = listing.xpath('.//span[@id="address"]/text()').get(); 
            phone = listing.xpath('.//span[@id="phone"]/text()').get();
            
            yield {
                'name': name, 
                'address': address, 
                'phone': phone
            }

            # Define the next page 
            next_page = response.xpath('//div[@class="panel-footer"]/div[@class="pages"]//a[@class="bookNav next-page"]/@href').get()
            if next_page is not None: 
                yield response.follow(next_page, callback=self.parse);
