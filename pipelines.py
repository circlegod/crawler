# -*- coding: utf-8 -*-

from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class SheergirlPipeline(ImagesPipeline):

    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_path = [x["path"] for ok, x in results if ok]
        item["imagePath"] = self.IMAGES_STORE + "\\" + image_path[0]

        return item
