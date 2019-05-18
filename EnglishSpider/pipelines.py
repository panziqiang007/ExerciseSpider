# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class EnglishSpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO english_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class ChineseSpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO chinese_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class MathSpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO math_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class PhysicsSpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO physics_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class ChemistrySpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO chemistry_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class BiologySpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO biology_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class GeographySpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO geography_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class HistorySpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO history_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item


class PoliticsSpiderPipeline(object):

    db = pymysql.connect("localhost", "root", "0000", "exerciselib")

    cursor = db.cursor()

    def process_item(self, item, spider):

        if "yiji" not in item:
            yiji = ""
        else:
            yiji = item["yiji"][0].replace("'", "\"")

        if "erji" not in item:
            erji = ""
        else:
            erji = item["erji"][0].replace("'", "\"")

        if "content" not in item:
            content = ""
        else:
            content = item["content"][0].replace("'", "\"")

        if "answer" not in item:
            answer = ""
        else:
            answer = item["answer"][0].replace("'", "\"")

        if "analysis" not in item:
            analysis = ""
        else:
            analysis = item["analysis"][0].replace("'", "\"")

        sql = """INSERT INTO politics_lib (yiji, erji, content, answer, analysis) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (yiji, erji, content, answer, analysis)

        self.cursor.execute(sql)
        self.db.commit()
        return item
