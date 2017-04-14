/*
Navicat MySQL Data Transfer

Source Server         : DP_Aliyun_BJ
Source Server Version : 50627
Source Host           : 10.45.10.179:5506
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2017-04-14 16:25:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for date_test
-- ----------------------------
DROP TABLE IF EXISTS `date_test`;
CREATE TABLE `date_test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dayid` date DEFAULT NULL,
  `revenue` decimal(8,4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of date_test
-- ----------------------------
INSERT INTO `date_test` VALUES ('1', '2016-08-24', '5.6000');
INSERT INTO `date_test` VALUES ('2', '2016-08-25', '10.2300');
INSERT INTO `date_test` VALUES ('3', '2016-08-26', '1111.3000');
