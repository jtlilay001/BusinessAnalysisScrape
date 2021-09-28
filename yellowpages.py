import scrapy


class YellowpagesSpider(scrapy.Spider):
    name = 'yellowpages'
    allowed_domains = ['yellowpagecity.com']
    start_urls = ['http://www.yellowpagecity.com/US/NY/Flushing/Health+Clubs']

    def parse(self, response):
        businesses = response.xpath('//a[@class="listing-wrap"]');

        # Get the address and the phone numbr of the business. 
        for business in businesses: 
            name = business.xpath('.//span[@id="name"]/text()').get(); 
            address = business.xpath('.//span[@id="address"]/text()').get(); 
            phone = business.xpath('.//span[@id="phone"]/text()').get(); 

            yield {
                'business_name': name, 
                'address': address, 
                'phone': phone 
            } 

n
