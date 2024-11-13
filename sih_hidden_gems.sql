-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: sih
-- ------------------------------------------------------
-- Server version	8.3.0

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
-- Table structure for table `hidden_gems`
--

DROP TABLE IF EXISTS `hidden_gems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hidden_gems` (
  `statename` varchar(100) DEFAULT NULL,
  `placename` varchar(255) DEFAULT NULL,
  `img1` varchar(255) DEFAULT NULL,
  `img2` varchar(255) DEFAULT NULL,
  `img3` varchar(255) DEFAULT NULL,
  `lat` decimal(9,6) DEFAULT NULL,
  `lng` decimal(9,6) DEFAULT NULL,
  `id` int NOT NULL,
  `history` text,
  `info` text,
  `bg_img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hidden_gems`
--

LOCK TABLES `hidden_gems` WRITE;
/*!40000 ALTER TABLE `hidden_gems` DISABLE KEYS */;
INSERT INTO `hidden_gems` VALUES ('Uttarakhand','Chopta','C:\\devel\\better_sih\\static\\images\\hidden gems\\chopta\\istockphoto-532851471-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\chopta\\istockphoto-1150187031-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\chopta\\istockphoto-1174373085-612x612.jpg',30.345300,79.043700,1,'Located in the Kedarkhand region, Chopta has long been a pilgrimage route to the Kedarnath Temple. The region is deeply connected with ancient Hindu legends and spiritual practices. It serves as a base for treks to the Tungnath Temple, one of the highest Shiva temples in the world.','Often referred to as the \"Mini Switzerland of India,\" Chopta is a picturesque high-altitude meadow surrounded by dense forests and snow-capped peaks.','C:\\devel\\better_sih\\static\\images\\hidden gems\\chopta\\cover.jpg'),('Rajasthan','Bundi Stepwells','C:\\devel\\better_sih\\static\\images\\hidden gems\\bundi stepwell\\istockphoto-1206473060-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\bundi stepwell\\istockphoto-1265613766-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\bundi stepwell\\istockphoto-1285193680-612x612.jpg',25.430000,75.640000,2,'Bundi, a small town in Rajasthan, is known for its stunning stepwells, which are architectural marvels designed to provide water in the arid desert climate. They reflect the advanced water management techniques and architectural skills of the Rajput era.','The stepwells of Bundi were constructed between the 15th and 17th centuries under the patronage of local rulers. These intricately carved structures, like the Rani Ji Ki Baori, showcase the artistic heritage of the region.','C:\\devel\\better_sih\\static\\images\\hidden gems\\bundi stepwell\\cover.jpg'),('Karnataka','Hampi\'s Underground Temple','C:\\devel\\better_sih\\static\\images\\hidden gems\\hampi underground temple\\istockphoto-908944268-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\hampi underground temple\\istockphoto-915493730-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\hampi underground temple\\istockphoto-2159300497-612x612.jpg',15.335000,76.460000,3,'Built in the 15th century during the reign of the Vijayanagara Empire, the Underground Temple is believed to have been used for secret rituals or as a refuge during conflicts, adding a layer of mystery to its historical significance. It is one of the lesser-visited ruins but offers insight into the artistic achievements of the Vijayanagara Empire.','The Underground Temple in Hampi is a hidden gem with its subterranean architecture, featuring intricate carvings and a unique design.','C:\\devel\\better_sih\\static\\images\\hidden gems\\hampi underground temple\\cover.jpg'),('Assam','Majuli\'s Satras','C:\\devel\\better_sih\\static\\images\\hidden gems\\majuli satras\\istockphoto-1051314560-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\majuli satras\\istockphoto-1220650010-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\majuli satras\\istockphoto-1327495553-612x612.jpg',26.944400,94.217500,4,'Founded in the 15th century by Srimanta Sankardev, the satras of Majuli have been centers of Assamese culture and spirituality. They have preserved ancient art forms and traditional practices unique to the region. These satras are lesser-known but offer a deep dive into Assamese art, dance, and religious practices.','Majuli, the world?s largest river island, is home to several satras (monastic institutions) that are rich in Vaishnavite culture and traditions.','C:\\devel\\better_sih\\static\\images\\hidden gems\\majuli satras\\cover.jpg'),('Odisha','Chandipur Beach','C:\\devel\\better_sih\\static\\images\\hidden gems\\chandipur beach\\istockphoto-638035312-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\chandipur beach\\istockphoto-1329889142-612x612.jpg','C:\\devel\\better_sih\\static\\images\\hidden gems\\chandipur beach\\istockphoto-2150543265-612x612.jpg',21.473500,87.019300,5,'Chandipur Beach is known for its unique phenomenon where the sea recedes up to 5 kilometers during low tide, creating a vast expanse of sand. This natural marvel is relatively lesser known but offers a glimpse into the dynamic coastal landscape of Odisha.','Chandipur Beach is known for its unique phenomenon where the sea recedes up to 5 kilometers during low tide, creating a vast expanse of sand.','C:\\devel\\better_sih\\static\\images\\hidden gems\\chandipur beach\\cover.jpg');
/*!40000 ALTER TABLE `hidden_gems` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-13 20:39:59
