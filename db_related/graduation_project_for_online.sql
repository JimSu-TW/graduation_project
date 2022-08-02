-- MySQL Script generated by MySQL Workbench
-- Mon Jul 18 22:40:43 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_108403547
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_108403547
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_108403547` DEFAULT CHARACTER SET utf8 ;
USE `db_108403547` ;

-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_icon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_icon` (
  `icon_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `link` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`icon_id`),
  UNIQUE INDEX `icon_id_UNIQUE` (`icon_id` ASC) VISIBLE,
  UNIQUE INDEX `link_UNIQUE` (`link` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_source`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_source` (
  `source_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `icon_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`source_id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  UNIQUE INDEX `source_id_UNIQUE` (`source_id` ASC) VISIBLE,
  UNIQUE INDEX `icon_id_UNIQUE` (`icon_id` ASC) VISIBLE,
  CONSTRAINT `icon_to_source_fk`
    FOREIGN KEY (`icon_id`)
    REFERENCES `db_108403547`.`tbl_icon` (`icon_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_product_class`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_product_class` (
  `product_class_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`product_class_id`),
  UNIQUE INDEX `product_class_id_UNIQUE` (`product_class_id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_brand` (
  `brand_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `brand_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`brand_id`),
  UNIQUE INDEX `brand_id_UNIQUE` (`brand_id` ASC) VISIBLE,
  UNIQUE INDEX `brand_name_UNIQUE` (`brand_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_product` (
  `product_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `icon_id` INT UNSIGNED NOT NULL,
  `brand_id` INT UNSIGNED NOT NULL,
  `product_class_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `release_date` DATETIME NOT NULL,
  `specification` VARCHAR(1000) NULL,
  `create_date` DATETIME NOT NULL,
  `modified_date` DATETIME NOT NULL,
  PRIMARY KEY (`product_id`),
  UNIQUE INDEX `product_id_UNIQUE` (`product_id` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  UNIQUE INDEX `icon_link_UNIQUE` (`icon_id` ASC) VISIBLE,
  INDEX `product_class_to_product_id_idx` (`product_class_id` ASC) VISIBLE,
  INDEX `brand_to_product_fk_idx` (`brand_id` ASC) VISIBLE,
  CONSTRAINT `icon_to_product_fk`
    FOREIGN KEY (`icon_id`)
    REFERENCES `db_108403547`.`tbl_icon` (`icon_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `product_class_to_product_id`
    FOREIGN KEY (`product_class_id`)
    REFERENCES `db_108403547`.`tbl_product_class` (`product_class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `brand_to_product_fk`
    FOREIGN KEY (`brand_id`)
    REFERENCES `db_108403547`.`tbl_brand` (`brand_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_post`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_post` (
  `post_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `source_id` INT UNSIGNED NOT NULL,
  `product_id` INT UNSIGNED NOT NULL,
  `title` VARCHAR(100) NOT NULL,
  `link` VARCHAR(300) NOT NULL,
  `date` DATETIME NOT NULL,
  `content` TEXT NULL,
  `create_date` DATETIME NOT NULL,
  `modified_date` DATETIME NULL,
  PRIMARY KEY (`post_id`),
  UNIQUE INDEX `post_id_UNIQUE` (`post_id` ASC) VISIBLE,
  UNIQUE INDEX `title_UNIQUE` (`title` ASC) VISIBLE,
  UNIQUE INDEX `link_UNIQUE` (`link` ASC) VISIBLE,
  INDEX `source_to_post_fk_idx` (`source_id` ASC) VISIBLE,
  INDEX `product_to_post_fk_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `source_to_post_fk`
    FOREIGN KEY (`source_id`)
    REFERENCES `db_108403547`.`tbl_source` (`source_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT,
  CONSTRAINT `product_to_post_fk`
    FOREIGN KEY (`product_id`)
    REFERENCES `db_108403547`.`tbl_product` (`product_id`)
    ON DELETE RESTRICT
    ON UPDATE RESTRICT)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_label`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_label` (
  `label_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_class_id` INT UNSIGNED NOT NULL,
  `icon_id` INT UNSIGNED NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`label_id`),
  UNIQUE INDEX `product_class_id_UNIQUE` (`product_class_id` ASC) VISIBLE,
  UNIQUE INDEX `label_id_UNIQUE` (`label_id` ASC) VISIBLE,
  UNIQUE INDEX `icon_id_UNIQUE` (`icon_id` ASC) VISIBLE,
  CONSTRAINT `product_class_to_label_fk`
    FOREIGN KEY (`product_class_id`)
    REFERENCES `db_108403547`.`tbl_product_class` (`product_class_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `icon_to_label_fk`
    FOREIGN KEY (`icon_id`)
    REFERENCES `db_108403547`.`tbl_icon` (`icon_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_108403547`.`tbl_label_detail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_108403547`.`tbl_label_detail` (
  `label_detail_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_id` INT UNSIGNED NOT NULL,
  `label_id` INT UNSIGNED NOT NULL,
  `content` VARCHAR(45) NOT NULL,
  `create_date` DATETIME NOT NULL,
  `modified_date` DATETIME NULL,
  PRIMARY KEY (`label_detail_id`),
  UNIQUE INDEX `label_detail_id_UNIQUE` (`label_detail_id` ASC) VISIBLE,
  UNIQUE INDEX `product_id_UNIQUE` (`product_id` ASC) VISIBLE,
  INDEX `label_to_label_detail_fk_idx` (`label_id` ASC) VISIBLE,
  CONSTRAINT `product_to_label_detail_fk`
    FOREIGN KEY (`product_id`)
    REFERENCES `db_108403547`.`tbl_product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `label_to_label_detail_fk`
    FOREIGN KEY (`label_id`)
    REFERENCES `db_108403547`.`tbl_label` (`label_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;