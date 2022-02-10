-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 10, 2022 at 02:45 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rms`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_meal`
--

DROP TABLE IF EXISTS `customer_meal`;
CREATE TABLE IF NOT EXISTS `customer_meal` (
  `customername` varchar(100) NOT NULL,
  `fmeal` varchar(100) NOT NULL,
  `lmeal` varchar(100) NOT NULL,
  `pbmeal` varchar(100) NOT NULL,
  `pizzameal` varchar(100) NOT NULL,
  `cheezemeal` varchar(100) NOT NULL,
  `drinkmeal` varchar(100) NOT NULL,
  `orderno` varchar(100) NOT NULL,
  `costofmeal` varchar(100) NOT NULL,
  `surcharge` varchar(100) NOT NULL,
  `taxcharge` varchar(100) NOT NULL,
  `totalpay` varchar(100) NOT NULL,
  `timed_ate` varchar(100) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `customer_meal`
--

INSERT INTO `customer_meal` (`customername`, `fmeal`, `lmeal`, `pbmeal`, `pizzameal`, `cheezemeal`, `drinkmeal`, `orderno`, `costofmeal`, `surcharge`, `taxcharge`, `totalpay`, `timed_ate`) VALUES
('', '1', '1', '1', '1', '1', '1', '17958653523', '278', '2.808080808080808', '50.04', '330.84808080808085', ''),
('', '2', '1', '1', '1', '1', '0', '38851425149', '283', '2.8585858585858586', '50.94', '336.79858585858585', '10-February-2022	11:22:15  AM'),
('Ashutosh Prasad', '11', '3', '3', '3', '3', '3', '46673594015', '1234', '12.464646464646465', '222.12', '1468.5846464646465', '10-February-2022	11:35:52  AM'),
('Rahul Dubey', '1', '1', '0', '0', '0', '1', '17628726585', '144', '1.4545454545454546', '25.919999999999998', '171.37454545454545', '10-February-2022	11:37:56  AM');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
