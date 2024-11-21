-- MySQL dump 10.13  Distrib 8.0.21, for osx10.15 (x86_64)
--
-- Host: localhost    Database: Millionaire
-- ------------------------------------------------------
-- Server version    5.7.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dynamic`
--

USE Millionaire;

DROP TABLE IF EXISTS `dynamic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dynamic` (
  `Question` varchar(255) DEFAULT NULL,
  `Ans1` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `Ans2` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `Ans3` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `Ans4` varchar(255) CHARACTER SET utf8 DEFAULT NULL,
  `Correct` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dynamic`
--

LOCK TABLES `dynamic` WRITE;
/*!40000 ALTER TABLE `dynamic` DISABLE KEYS */;
INSERT INTO `dynamic`
VALUES
("Which of the following is a strong password?", "Password123", "123456", "SunnyDay!", "ABCDEFG", 2);
/*!40000 ALTER TABLE `dynamic` ENABLE KEYS */;
UNLOCK TABLES;
