import scrapy


class SwitchSpider(scrapy.Spider):
    name = "ns"

    def start_requests(self):
        urls = [
            'https://www.famitsu.com/schedule/switch/?dl=0',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     filename = 'index.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file %s' % filename)

    def parse(self, response):
        filename = 'schedule.txt'

        dates = []
        for d in response.css("h2.heading__title"):
            date = d.css("h2.heading__title::text").get()
            dates.append(date)

        titles = []
        temp = ""
        for dts in response.css("div.row.schedule-row"):
            for ts in dts.css("span.card-schedule__title-inline"):
                t = ts.css("span.card-schedule__title-inline::text").get()
                # TODO If t is none?
                temp = temp + t + ","
            titles.append(temp)
            temp = ""

        with open(filename, 'w') as f:
            for i in range(len(dates)):
                f.write(dates[i])
                f.write("\n")

                tmp_titles = titles[i].split(',')
                for j in range(len(tmp_titles)):
                    f.write(tmp_titles[j])
                    f.write("\n")