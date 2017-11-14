/*
 Navicat MySQL Data Transfer

 Source Server         : 192.168.36.80
 Source Server Type    : MySQL
 Source Server Version : 50720
 Source Host           : 192.168.36.80
 Source Database       : gyp_test

 Target Server Type    : MySQL
 Target Server Version : 50720
 File Encoding         : utf-8

 Date: 10/29/2017 16:43:29 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `weibo_user`
-- ----------------------------
DROP TABLE IF EXISTS `weibo_user`;
CREATE TABLE `weibo_user` (
  `keyword` varchar(100) COLLATE utf8_bin NOT NULL,
  `cover` varchar(250) COLLATE utf8_bin NOT NULL,
  `nick_name` varchar(100) COLLATE utf8_bin NOT NULL,
  `digest` varchar(500) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

SET FOREIGN_KEY_CHECKS = 1;
