-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 24, 2022 at 06:17 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `frdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add buyer_reg_tb', 7, 'add_buyer_reg_tb'),
(26, 'Can change buyer_reg_tb', 7, 'change_buyer_reg_tb'),
(27, 'Can delete buyer_reg_tb', 7, 'delete_buyer_reg_tb'),
(28, 'Can view buyer_reg_tb', 7, 'view_buyer_reg_tb'),
(29, 'Can add seller_reg_tb', 8, 'add_seller_reg_tb'),
(30, 'Can change seller_reg_tb', 8, 'change_seller_reg_tb'),
(31, 'Can delete seller_reg_tb', 8, 'delete_seller_reg_tb'),
(32, 'Can view seller_reg_tb', 8, 'view_seller_reg_tb'),
(33, 'Can add admin_tb', 9, 'add_admin_tb'),
(34, 'Can change admin_tb', 9, 'change_admin_tb'),
(35, 'Can delete admin_tb', 9, 'delete_admin_tb'),
(36, 'Can view admin_tb', 9, 'view_admin_tb'),
(37, 'Can add f_bokking_tb', 10, 'add_f_bokking_tb'),
(38, 'Can change f_bokking_tb', 10, 'change_f_bokking_tb'),
(39, 'Can delete f_bokking_tb', 10, 'delete_f_bokking_tb'),
(40, 'Can view f_bokking_tb', 10, 'view_f_bokking_tb'),
(41, 'Can add category_tb', 11, 'add_category_tb'),
(42, 'Can change category_tb', 11, 'change_category_tb'),
(43, 'Can delete category_tb', 11, 'delete_category_tb'),
(44, 'Can view category_tb', 11, 'view_category_tb'),
(45, 'Can add f_details_tb', 12, 'add_f_details_tb'),
(46, 'Can change f_details_tb', 12, 'change_f_details_tb'),
(47, 'Can delete f_details_tb', 12, 'delete_f_details_tb'),
(48, 'Can view f_details_tb', 12, 'view_f_details_tb');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'freeapp', 'admin_tb'),
(7, 'freeapp', 'buyer_reg_tb'),
(11, 'freeapp', 'category_tb'),
(10, 'freeapp', 'f_bokking_tb'),
(12, 'freeapp', 'f_details_tb'),
(8, 'freeapp', 'seller_reg_tb'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-29 07:35:25.007077'),
(2, 'auth', '0001_initial', '2022-10-29 07:35:27.892619'),
(3, 'admin', '0001_initial', '2022-10-29 07:35:28.502161'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-10-29 07:35:28.549044'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-29 07:35:28.602452'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-10-29 07:35:29.034390'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-10-29 07:35:29.318697'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-10-29 07:35:29.402849'),
(9, 'auth', '0004_alter_user_username_opts', '2022-10-29 07:35:29.449885'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-10-29 07:35:30.048430'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-10-29 07:35:30.064063'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-29 07:35:30.105850'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-10-29 07:35:30.183991'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-29 07:35:30.253027'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-10-29 07:35:30.368954'),
(16, 'auth', '0011_update_proxy_permissions', '2022-10-29 07:35:30.406233'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-29 07:35:30.506556'),
(18, 'freeapp', '0001_initial', '2022-10-29 07:35:30.708371'),
(19, 'sessions', '0001_initial', '2022-10-29 07:35:31.515856'),
(20, 'freeapp', '0002_remove_buyer_reg_tb_cpassword_and_more', '2022-10-30 04:34:22.246447'),
(21, 'freeapp', '0003_admin_tb_category_tb_f_details_tb_f_bokking_tb', '2022-10-30 06:22:42.214099');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('00ffh06idgofvh9s6ps71k2yqkdaz0vd', 'e30:1op4mt:ASzUcll3szNzwR1zwFVL6TDHp1XJ4iAYpb-jCs5b3Qc', '2022-11-13 09:39:27.707627'),
('7bx47umrcxy3b1xon59b3kjxarosll4f', 'eyJidWlkIjo0fQ:1p8vsw:jyMpJMFG_Cv_2DowFbK1HnCFjIgIOrA0B6Q0GDWNYNU', '2023-01-07 04:11:46.203603'),
('7xm68xpcroowujtrw9vr4wn97n1dycvl', 'e30:1opfw4:sbkYBQahu8OFoTEe6mmp2pSFVIyyWJb7OfpVgqrxl6g', '2022-11-15 01:19:24.279266');

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_admin_tb`
--

CREATE TABLE `freeapp_admin_tb` (
  `id` bigint(20) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `freeapp_admin_tb`
--

INSERT INTO `freeapp_admin_tb` (`id`, `Email`, `Password`) VALUES
(1, 'admin@gmail.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_buyer_reg_tb`
--

CREATE TABLE `freeapp_buyer_reg_tb` (
  `id` bigint(20) NOT NULL,
  `Fname` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Address` varchar(15) NOT NULL,
  `District` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `freeapp_buyer_reg_tb`
--

INSERT INTO `freeapp_buyer_reg_tb` (`id`, `Fname`, `Email`, `Password`, `Phone`, `Address`, `District`) VALUES
(1, 'zx', 'admin@gmail.com', '123', '6543', 'gfds', 'fd'),
(2, 'fghj', 'admfhnhyin@gmail.com', '12345', '1234567890', 'qwertjklfghiop', 'fd'),
(3, 'mucg', 'adwfghmin@gmail.com', '12345', '123457890', 'qwedfghjkl', 'kasarkode'),
(4, 'dilsh', 'dilsh@gmail.com', '12345', '1234567890', 'qwertyuiop[ asd', 'kasarkode');

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_category_tb`
--

CREATE TABLE `freeapp_category_tb` (
  `id` bigint(20) NOT NULL,
  `Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `freeapp_category_tb`
--

INSERT INTO `freeapp_category_tb` (`id`, `Name`) VALUES
(1, 'cloth'),
(2, 'BOOKS'),
(3, 'HEALTH AND FITNESS'),
(4, 'KIDS'),
(5, 'LIFESTYLE'),
(6, 'MEDICAL'),
(7, 'MUSIC'),
(8, 'SPORTS'),
(9, 'FURNITURE'),
(10, 'KITCHEN ACCESSORIES'),
(11, 'LAWN NDD GARDENING'),
(12, ''),
(13, 'LAWN AND GARDENING'),
(14, 'PHONE AND ACCESSORIES'),
(15, 'JWELLERY'),
(16, 'BEAUTY');

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_f_bokking_tb`
--

CREATE TABLE `freeapp_f_bokking_tb` (
  `id` bigint(20) NOT NULL,
  `Date` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `Buyer_id` bigint(20) NOT NULL,
  `Free_details_id` bigint(20) NOT NULL,
  `Seller_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_f_details_tb`
--

CREATE TABLE `freeapp_f_details_tb` (
  `id` bigint(20) NOT NULL,
  `Title` varchar(100) NOT NULL,
  `File` varchar(100) NOT NULL,
  `Describtion` varchar(300) NOT NULL,
  `Date` varchar(100) NOT NULL,
  `Price` varchar(100) NOT NULL,
  `Status` varchar(100) NOT NULL,
  `Catname_id` bigint(20) NOT NULL,
  `Seller_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `freeapp_f_details_tb`
--

INSERT INTO `freeapp_f_details_tb` (`id`, `Title`, `File`, `Describtion`, `Date`, `Price`, `Status`, `Catname_id`, `Seller_id`) VALUES
(1, 'bag', 'freestuff_details/WhatsApp_Image_2022-10-22_at_10.26.17_AM_2.jpeg', 'qwertyuio asdfghjk xcvbnm dfghjk dfghjk', '2022-12-10 10:17:09.175433', 'Free stuff', 'Pending', 1, 1),
(2, 'Harrypotter', 'freestuff_details/download.jpeg', 'qwertyuio asdfghjk xcvbnm dfghjk dfghjk', '2022-12-10 11:51:05.223889', 'Free stuff', 'Pending', 2, 1),
(3, 'Nike shoe', 'freestuff_details/images.jpg', 'wertyufgh', '2022-12-10 11:51:54.504128', 'Free stuff', 'Pending', 5, 1),
(4, 'table', 'freestuff_details/table.jpg', 'qwertyuio asdfghjk xcvbnm dfghjk dfghjk', '2022-12-10 11:52:51.635817', 'Free stuff', 'Pending', 9, 1),
(5, 'ewr', 'freestuff_details/bag2.jpg', 'wertyufgh', '2022-12-10 11:55:09.233510', 'Free stuff', 'Pending', 14, 1),
(6, 'rtyu', 'freestuff_details/b16893b8-3b4b-443e-99fe-e95cb8b35da4.jpg', 'qs', '2022-12-10 12:20:58.666544', 'Free stuff', 'Pending', 2, 1),
(7, 'TTT', 'freestuff_details/bag1.jpg', 'SDF', '2022-12-10 12:28:25.489195', 'Free stuff', 'Pending', 8, 1),
(8, 'TTT', 'freestuff_details/bag1_p8Mp2ZM.jpg', 'SDF', '2022-12-10 12:28:43.944836', 'Free stuff', 'Pending', 8, 1),
(9, 'dffd', 'freestuff_details/images_ioZUftQ.jpg', 'sd', '2022-12-10 12:44:04.669144', 'Free stuff', 'Pending', 16, 1),
(10, 'sdfgw', 'freestuff_details/table_2sjuTcZ.jpg', 'dwdwwd', '2022-12-10 12:56:14.478961', '321', 'Pending', 15, 1),
(11, 'harryporter', 'freestuff_details/download_hkH7OQu.jpeg', 'qwertyuio asdfghjk xcvbnm dfghjk dfghjk', '2022-12-10 14:18:44.856737', '230', 'Pending', 2, 1);

-- --------------------------------------------------------

--
-- Table structure for table `freeapp_seller_reg_tb`
--

CREATE TABLE `freeapp_seller_reg_tb` (
  `id` bigint(20) NOT NULL,
  `Fname` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Address` varchar(15) NOT NULL,
  `District` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `freeapp_seller_reg_tb`
--

INSERT INTO `freeapp_seller_reg_tb` (`id`, `Fname`, `Email`, `Password`, `Phone`, `Address`, `District`) VALUES
(1, 'muhammed p', 'muhammedp@gmail.com', '12345', '0987654321', 'qwertyuiop[ asd', 'kannur');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `freeapp_admin_tb`
--
ALTER TABLE `freeapp_admin_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `freeapp_buyer_reg_tb`
--
ALTER TABLE `freeapp_buyer_reg_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `freeapp_category_tb`
--
ALTER TABLE `freeapp_category_tb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `freeapp_f_bokking_tb`
--
ALTER TABLE `freeapp_f_bokking_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `freeapp_f_bokking_tb_Buyer_id_46a5f7b6_fk_freeapp_b` (`Buyer_id`),
  ADD KEY `freeapp_f_bokking_tb_Free_details_id_76cf21b6_fk_freeapp_f` (`Free_details_id`),
  ADD KEY `freeapp_f_bokking_tb_Seller_id_44adca40_fk_freeapp_s` (`Seller_id`);

--
-- Indexes for table `freeapp_f_details_tb`
--
ALTER TABLE `freeapp_f_details_tb`
  ADD PRIMARY KEY (`id`),
  ADD KEY `freeapp_f_details_tb_Catname_id_f1d43f63_fk_freeapp_c` (`Catname_id`),
  ADD KEY `freeapp_f_details_tb_Seller_id_eb5e49e4_fk_freeapp_s` (`Seller_id`);

--
-- Indexes for table `freeapp_seller_reg_tb`
--
ALTER TABLE `freeapp_seller_reg_tb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `freeapp_admin_tb`
--
ALTER TABLE `freeapp_admin_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `freeapp_buyer_reg_tb`
--
ALTER TABLE `freeapp_buyer_reg_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `freeapp_category_tb`
--
ALTER TABLE `freeapp_category_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `freeapp_f_bokking_tb`
--
ALTER TABLE `freeapp_f_bokking_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `freeapp_f_details_tb`
--
ALTER TABLE `freeapp_f_details_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `freeapp_seller_reg_tb`
--
ALTER TABLE `freeapp_seller_reg_tb`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `freeapp_f_bokking_tb`
--
ALTER TABLE `freeapp_f_bokking_tb`
  ADD CONSTRAINT `freeapp_f_bokking_tb_Buyer_id_46a5f7b6_fk_freeapp_b` FOREIGN KEY (`Buyer_id`) REFERENCES `freeapp_buyer_reg_tb` (`id`),
  ADD CONSTRAINT `freeapp_f_bokking_tb_Free_details_id_76cf21b6_fk_freeapp_f` FOREIGN KEY (`Free_details_id`) REFERENCES `freeapp_f_details_tb` (`id`),
  ADD CONSTRAINT `freeapp_f_bokking_tb_Seller_id_44adca40_fk_freeapp_s` FOREIGN KEY (`Seller_id`) REFERENCES `freeapp_seller_reg_tb` (`id`);

--
-- Constraints for table `freeapp_f_details_tb`
--
ALTER TABLE `freeapp_f_details_tb`
  ADD CONSTRAINT `freeapp_f_details_tb_Catname_id_f1d43f63_fk_freeapp_c` FOREIGN KEY (`Catname_id`) REFERENCES `freeapp_category_tb` (`id`),
  ADD CONSTRAINT `freeapp_f_details_tb_Seller_id_eb5e49e4_fk_freeapp_s` FOREIGN KEY (`Seller_id`) REFERENCES `freeapp_seller_reg_tb` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
