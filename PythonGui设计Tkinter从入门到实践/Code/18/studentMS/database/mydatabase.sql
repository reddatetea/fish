-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: mydatabase
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tb_class`
--

DROP TABLE IF EXISTS `tb_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_class` (
  `classID` int NOT NULL,
  `gradeID` int NOT NULL,
  `className` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`classID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_class`
--

LOCK TABLES `tb_class` WRITE;
/*!40000 ALTER TABLE `tb_class` DISABLE KEYS */;
INSERT INTO `tb_class` VALUES (1,1,'一班'),(2,1,'二班'),(3,1,'三班'),(4,2,'一班'),(5,2,'二班'),(6,2,'三班'),(7,3,'一班'),(8,3,'二班'),(9,3,'三班');
/*!40000 ALTER TABLE `tb_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_examkinds`
--

DROP TABLE IF EXISTS `tb_examkinds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_examkinds` (
  `kindID` int NOT NULL,
  `kindName` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`kindID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_examkinds`
--

LOCK TABLES `tb_examkinds` WRITE;
/*!40000 ALTER TABLE `tb_examkinds` DISABLE KEYS */;
INSERT INTO `tb_examkinds` VALUES (1,'期中考试'),(2,'期末考试');
/*!40000 ALTER TABLE `tb_examkinds` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_grade`
--

DROP TABLE IF EXISTS `tb_grade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_grade` (
  `gradeID` int NOT NULL DEFAULT '1',
  `gradeName` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`gradeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_grade`
--

LOCK TABLES `tb_grade` WRITE;
/*!40000 ALTER TABLE `tb_grade` DISABLE KEYS */;
INSERT INTO `tb_grade` VALUES (1,'初一'),(2,'初二'),(3,'初三');
/*!40000 ALTER TABLE `tb_grade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_result`
--

DROP TABLE IF EXISTS `tb_result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_result` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `stuID` varchar(20) DEFAULT NULL,
  `kindID` int DEFAULT NULL,
  `subID` int DEFAULT NULL,
  `result` double DEFAULT '0',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_result`
--

LOCK TABLES `tb_result` WRITE;
/*!40000 ALTER TABLE `tb_result` DISABLE KEYS */;
INSERT INTO `tb_result` VALUES (1,'BS0101001',1,1,90),(2,'BS0101001',1,2,80),(3,'BS0101001',1,3,100),(4,'BS0101002',1,3,100),(5,'BS0101002',1,1,90),(6,'BS0101002',1,2,98),(8,'BS0010101',1,2,80),(9,'BS0010102',1,2,79),(10,'BS0010102',1,3,90),(11,'BS0010101',1,3,95),(12,'BS0010101',1,4,90),(13,'BS0010102',1,4,95);
/*!40000 ALTER TABLE `tb_result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_student`
--

DROP TABLE IF EXISTS `tb_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_student` (
  `stuID` varchar(20) NOT NULL DEFAULT 'SID00101001',
  `stuName` varchar(20) DEFAULT NULL,
  `classID` int DEFAULT NULL,
  `gradeID` int DEFAULT NULL,
  `age` int DEFAULT NULL,
  `sex` char(4) DEFAULT NULL,
  `phone` char(20) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`stuID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_student`
--

LOCK TABLES `tb_student` WRITE;
/*!40000 ALTER TABLE `tb_student` DISABLE KEYS */;
INSERT INTO `tb_student` VALUES ('BS0010101','张佳',1,1,12,'女','11000000000','陕西西安'),('BS0010102','王磊',1,1,12,'男','11000000000','吉林长春'),('BS0010201','王蕾',2,1,12,'女','13000000000','吉林省长春市'),('BS0010202','张庭',2,1,12,'男','13000000000','山西省长治市'),('BS0010301','韩蕊',3,1,12,'女','13000000000','辽宁省沈阳市'),('BS0010302','李好',3,1,12,'男','13000000000','辽宁省大连市'),('BS0020101','冯涟',4,2,13,'女','1300000000','北京市朝阳区'),('BS0020102','张小北',4,2,13,'男','1300000000','北京市朝阳区'),('BS0020201','杨昊',5,2,13,'男','13000000000','山西省太原市'),('BS0020202','章雯',5,2,13,'女','13000000000','山西省太原市'),('BS0020301','王琦',6,2,13,'男','13000000000','吉林省长春市'),('BS0020302','杨珂',6,2,13,'女','13000000000','吉林省长春市'),('BS0030101','梁雪',7,3,14,'男','13000000000','湖南省长沙市'),('BS0030102','朱茱',7,3,14,'女','13000000000','湖南省长沙市'),('BS0030201','杨婧',8,3,14,'女','13000000000','广东省广州市'),('BS0030202','杨庭',8,3,14,'男','13000000000','广东省广州市'),('BS0030301','王石',9,3,14,'男','1300000000','江苏省苏州市'),('BS0030302','王诗诗',9,3,14,'女','13000000000','江苏省无锡市');
/*!40000 ALTER TABLE `tb_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_subject`
--

DROP TABLE IF EXISTS `tb_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_subject` (
  `subID` int NOT NULL,
  `subName` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`subID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_subject`
--

LOCK TABLES `tb_subject` WRITE;
/*!40000 ALTER TABLE `tb_subject` DISABLE KEYS */;
INSERT INTO `tb_subject` VALUES (1,'数学'),(2,'语文'),(3,'计算机'),(4,'英语');
/*!40000 ALTER TABLE `tb_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tb_user`
--

DROP TABLE IF EXISTS `tb_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tb_user` (
  `userName` varchar(20) NOT NULL,
  `userPwd` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`userName`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tb_user`
--

LOCK TABLES `tb_user` WRITE;
/*!40000 ALTER TABLE `tb_user` DISABLE KEYS */;
INSERT INTO `tb_user` VALUES ('mr','mrsoft');
/*!40000 ALTER TABLE `tb_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `v_classinfo`
--

DROP TABLE IF EXISTS `v_classinfo`;
/*!50001 DROP VIEW IF EXISTS `v_classinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_classinfo` AS SELECT 
 1 AS `classID`,
 1 AS `gradeID`,
 1 AS `gradeName`,
 1 AS `className`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_resultinfo`
--

DROP TABLE IF EXISTS `v_resultinfo`;
/*!50001 DROP VIEW IF EXISTS `v_resultinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_resultinfo` AS SELECT 
 1 AS `ID`,
 1 AS `stuID`,
 1 AS `stuName`,
 1 AS `kindName`,
 1 AS `subName`,
 1 AS `className`,
 1 AS `gradeName`,
 1 AS `result`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `v_studentinfo`
--

DROP TABLE IF EXISTS `v_studentinfo`;
/*!50001 DROP VIEW IF EXISTS `v_studentinfo`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `v_studentinfo` AS SELECT 
 1 AS `stuID`,
 1 AS `stuName`,
 1 AS `age`,
 1 AS `sex`,
 1 AS `phone`,
 1 AS `address`,
 1 AS `className`,
 1 AS `gradeName`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_classinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_classinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_classinfo` AS select `tb_class`.`classID` AS `classID`,`tb_grade`.`gradeID` AS `gradeID`,`tb_grade`.`gradeName` AS `gradeName`,`tb_class`.`className` AS `className` from (`tb_class` join `tb_grade`) where (`tb_class`.`gradeID` = `tb_grade`.`gradeID`) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_resultinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_resultinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_resultinfo` AS select `tb_result`.`ID` AS `ID`,`tb_result`.`stuID` AS `stuID`,`v_studentinfo`.`stuName` AS `stuName`,`tb_examkinds`.`kindName` AS `kindName`,`tb_subject`.`subName` AS `subName`,`v_studentinfo`.`className` AS `className`,`v_studentinfo`.`gradeName` AS `gradeName`,`tb_result`.`result` AS `result` from (((`tb_subject` join `tb_result`) join `tb_examkinds`) join `v_studentinfo`) where ((`tb_result`.`stuID` = `v_studentinfo`.`stuID`) and (`tb_result`.`kindID` = `tb_examkinds`.`kindID`) and (`tb_result`.`subID` = `tb_subject`.`subID`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `v_studentinfo`
--

/*!50001 DROP VIEW IF EXISTS `v_studentinfo`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_studentinfo` AS select `tb_student`.`stuID` AS `stuID`,`tb_student`.`stuName` AS `stuName`,`tb_student`.`age` AS `age`,`tb_student`.`sex` AS `sex`,`tb_student`.`phone` AS `phone`,`tb_student`.`address` AS `address`,`tb_class`.`className` AS `className`,`tb_grade`.`gradeName` AS `gradeName` from ((`tb_student` join `tb_class`) join `tb_grade`) where ((`tb_student`.`classID` = `tb_class`.`classID`) and (`tb_student`.`gradeID` = `tb_grade`.`gradeID`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-05-13 17:35:35
