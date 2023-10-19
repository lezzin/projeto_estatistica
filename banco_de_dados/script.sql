-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema projeto_estatistica
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema projeto_estatistica
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `projeto_estatistica` DEFAULT CHARACTER SET utf8 ;
USE `projeto_estatistica` ;

-- -----------------------------------------------------
-- Table `projeto_estatistica`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `senha` TEXT NOT NULL,
  `tipo_usuario` ENUM('1', '2') NOT NULL,
  PRIMARY KEY (`idusuario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`contato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`contato` (
  `idcontato` INT NOT NULL AUTO_INCREMENT,
  `mensagem` VARCHAR(45) NOT NULL,
  `assunto` VARCHAR(45) NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  PRIMARY KEY (`idcontato`, `usuario_idusuario`),
  INDEX `fk_contato_usuario_idx` (`usuario_idusuario` ASC),
  CONSTRAINT `fk_contato_usuario`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `projeto_estatistica`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`materia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`materia` (
  `idmateria` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`idmateria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`exercicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`exercicio` (
  `idexercicio` INT NOT NULL AUTO_INCREMENT,
  `enunciado` VARCHAR(45) NOT NULL,
  `materia_idmateria` INT NOT NULL,
  PRIMARY KEY (`idexercicio`, `materia_idmateria`),
  INDEX `fk_exercicio_materia1_idx` (`materia_idmateria` ASC),
  CONSTRAINT `fk_exercicio_materia1`
    FOREIGN KEY (`materia_idmateria`)
    REFERENCES `projeto_estatistica`.`materia` (`idmateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`alternativa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`alternativa` (
  `idalternativa` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NOT NULL,
  `status` ENUM('correto', 'incorreto') NOT NULL,
  `exercicio_idexercicio` INT NOT NULL,
  `exercicio_materia_idmateria` INT NOT NULL,
  PRIMARY KEY (`idalternativa`, `exercicio_idexercicio`, `exercicio_materia_idmateria`),
  INDEX `fk_alternativa_exercicio1_idx` (`exercicio_idexercicio` ASC, `exercicio_materia_idmateria` ASC),
  CONSTRAINT `fk_alternativa_exercicio1`
    FOREIGN KEY (`exercicio_idexercicio` , `exercicio_materia_idmateria`)
    REFERENCES `projeto_estatistica`.`exercicio` (`idexercicio` , `materia_idmateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`pontuacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`pontuacao` (
  `idpontuacao` INT NOT NULL AUTO_INCREMENT,
  `quantidade` INT NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  `exercicio_idexercicio` INT NOT NULL,
  `exercicio_materia_idmateria` INT NOT NULL,
  PRIMARY KEY (`idpontuacao`, `usuario_idusuario`, `exercicio_idexercicio`, `exercicio_materia_idmateria`),
  INDEX `fk_pontuacao_usuario1_idx` (`usuario_idusuario` ASC),
  INDEX `fk_pontuacao_exercicio1_idx` (`exercicio_idexercicio` ASC, `exercicio_materia_idmateria` ASC),
  CONSTRAINT `fk_pontuacao_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `projeto_estatistica`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pontuacao_exercicio1`
    FOREIGN KEY (`exercicio_idexercicio` , `exercicio_materia_idmateria`)
    REFERENCES `projeto_estatistica`.`exercicio` (`idexercicio` , `materia_idmateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`resumo_atividade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`resumo_atividade` (
  `idresumo_atividade` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NOT NULL,
  `data` DATETIME NOT NULL,
  `usuario_idusuario` INT NOT NULL,
  PRIMARY KEY (`idresumo_atividade`, `usuario_idusuario`),
  INDEX `fk_resumo_atividade_usuario1_idx` (`usuario_idusuario` ASC),
  CONSTRAINT `fk_resumo_atividade_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `projeto_estatistica`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `projeto_estatistica`.`conteudo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `projeto_estatistica`.`conteudo` (
  `idconteudo` INT NULL AUTO_INCREMENT,
  `descricao` TEXT NOT NULL,
  `materia_idmateria` INT NOT NULL,
  PRIMARY KEY (`idconteudo`, `materia_idmateria`),
  INDEX `fk_conteudo_materia1_idx` (`materia_idmateria` ASC),
  CONSTRAINT `fk_conteudo_materia1`
    FOREIGN KEY (`materia_idmateria`)
    REFERENCES `projeto_estatistica`.`materia` (`idmateria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
