CREATE DATABASE  IF NOT EXISTS `TCM_BA` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `TCM_BA`;
-- MySQL dump 10.13  Distrib 5.6.13, for Win32 (x86)
--
-- Host: esfinge-hm.df.cgu    Database: TCM_BA
-- ------------------------------------------------------
-- Server version	5.5.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tcmba_contratos`
--

DROP TABLE IF EXISTS `tcmba_contratos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_contratos` (
  `idContrato` int(11) NOT NULL,
  `Unidade` int(11) DEFAULT NULL,
  `ExercicioAparente` int(11) DEFAULT NULL,
  `Contrato` varchar(25) DEFAULT NULL,
  `TipoContrato` varchar(50) DEFAULT NULL,
  `Moeda` varchar(25) DEFAULT NULL,
  `DataInicio` datetime DEFAULT NULL,
  `DataFim` datetime DEFAULT NULL,
  `CNPJ-CPF` varchar(20) DEFAULT NULL,
  `Fornecedor` varchar(100) DEFAULT NULL,
  `Licitacao` varchar(50) DEFAULT NULL,
  `DispInex` varchar(50) DEFAULT NULL,
  `Historico` longtext,
  `CredorNoAtiva` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idContrato`),
  KEY `idxUnidade` (`Unidade`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador da Unidade.',
  KEY `idxCNPJCPF` (`CNPJ-CPF`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador do credor (CNPJ ou CPF).',
  KEY `idxExercicio` (`ExercicioAparente`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_contratos`
--

/*!40000 ALTER TABLE `tcmba_contratos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_contratos` ENABLE KEYS */;

--
-- Table structure for table `tcmba_dispensasinexigibilidades`
--

DROP TABLE IF EXISTS `tcmba_dispensasinexigibilidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_dispensasinexigibilidades` (
  `idDispensaInexigibilidade` int(11) NOT NULL AUTO_INCREMENT,
  `Unidade` int(11) DEFAULT NULL,
  `ExercicioAparente` int(11) DEFAULT NULL,
  `Processo` varchar(50) DEFAULT NULL,
  `Fornecedor` varchar(100) DEFAULT NULL,
  `CNPJ-CPF` varchar(20) DEFAULT NULL,
  `Execucao` varchar(50) DEFAULT NULL,
  `Valor` double DEFAULT NULL,
  `Modalidade` varchar(50) DEFAULT NULL,
  `Historico` longtext,
  `CredorNoAtiva` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idDispensaInexigibilidade`),
  KEY `idxCNPJ-CPF` (`CNPJ-CPF`),
  KEY `idxUnidade` (`Unidade`),
  KEY `idxExercicioAparente` (`ExercicioAparente`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_dispensasinexigibilidades`
--

/*!40000 ALTER TABLE `tcmba_dispensasinexigibilidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_dispensasinexigibilidades` ENABLE KEYS */;

--
-- Table structure for table `tcmba_empenhos`
--

DROP TABLE IF EXISTS `tcmba_empenhos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_empenhos` (
  `idEmpenho` int(11) NOT NULL,
  `Unidade` int(11) DEFAULT NULL,
  `Exercicio` int(11) DEFAULT NULL,
  `Competencia` varchar(2) DEFAULT NULL,
  `Credor` varchar(100) DEFAULT NULL,
  `CNPJ-CPF` varchar(20) DEFAULT NULL,
  `Processo` varchar(50) DEFAULT NULL,
  `DataEmissao` datetime DEFAULT NULL,
  `Valor` double DEFAULT NULL,
  `Licitacao` varchar(50) DEFAULT NULL,
  `DispInex` varchar(50) DEFAULT NULL,
  `Contrato` varchar(25) DEFAULT NULL,
  `Orgao` varchar(75) DEFAULT NULL,
  `UnidadeOrcamentaria` varchar(75) DEFAULT NULL,
  `Funcao` varchar(25) DEFAULT NULL,
  `TipoAcao` varchar(25) DEFAULT NULL,
  `Acao` varchar(75) DEFAULT NULL,
  `Elemento` varchar(75) DEFAULT NULL,
  `FonteRecursos` varchar(100) DEFAULT NULL,
  `Historico` longtext,
  `CredorNoAtiva` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idEmpenho`),
  KEY `idxUnidade` (`Unidade`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador da Unidade.',
  KEY `idxCNPJCPF` (`CNPJ-CPF`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador do credor (CNPJ ou CPF).',
  KEY `idxDataEmissao` (`DataEmissao`) COMMENT 'Permitir consultas/ordenações mais rápidas pela data de emissão do empenho. '
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_empenhos`
--

/*!40000 ALTER TABLE `tcmba_empenhos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_empenhos` ENABLE KEYS */;

--
-- Table structure for table `tcmba_licitacoes`
--

DROP TABLE IF EXISTS `tcmba_licitacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_licitacoes` (
  `idLicitacao` int(11) NOT NULL AUTO_INCREMENT,
  `Unidade` int(11) DEFAULT NULL,
  `ExercicioHomologacao` int(11) DEFAULT NULL,
  `Processo` varchar(50) DEFAULT NULL,
  `DataHomologacao` datetime DEFAULT NULL,
  `Modalidade` varchar(50) DEFAULT NULL,
  `ValorEstimado` double DEFAULT NULL,
  `Objeto` longtext,
  `Execucao` varchar(50) DEFAULT NULL,
  `CNPJ-CPF` varchar(20) DEFAULT NULL,
  `Fornecedor` varchar(100) DEFAULT NULL,
  `ValorHomologado` double DEFAULT NULL,
  `CredorNoAtiva` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idLicitacao`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_licitacoes`
--

/*!40000 ALTER TABLE `tcmba_licitacoes` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_licitacoes` ENABLE KEYS */;

--
-- Table structure for table `tcmba_municipios`
--

DROP TABLE IF EXISTS `tcmba_municipios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_municipios` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Nome` varchar(50) DEFAULT NULL,
  `UF` varchar(2) DEFAULT NULL,
  `Regiao` varchar(2) DEFAULT NULL,
  `Populacao2011` int(11) DEFAULT NULL,
  `IBGE` int(11) DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `CodigoIBGE` (`IBGE`) COMMENT 'Permitir consultas mais rápidas a partir do código IBGE do Município. ',
  KEY `Nome` (`Nome`) COMMENT 'Permitir consultas mais rápidas pelo nome do Município. '
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_municipios`
--

/*!40000 ALTER TABLE `tcmba_municipios` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_municipios` ENABLE KEYS */;

--
-- Table structure for table `tcmba_pagamentos`
--

DROP TABLE IF EXISTS `tcmba_pagamentos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_pagamentos` (
  `idPagamento` int(11) NOT NULL AUTO_INCREMENT,
  `Unidade` int(11) DEFAULT NULL,
  `ExercicioPagamento` int(11) DEFAULT NULL,
  `Empenho` varchar(20) DEFAULT NULL,
  `Dotacao` varchar(50) DEFAULT NULL,
  `Processo` varchar(50) DEFAULT NULL,
  `Credor` varchar(100) DEFAULT NULL,
  `CNPJ-CPF` varchar(20) DEFAULT NULL,
  `DataEmpenho` datetime DEFAULT NULL,
  `DataPagamento` datetime DEFAULT NULL,
  `ValorPagamento` double DEFAULT NULL,
  `Retencao` double DEFAULT NULL,
  `ValorBruto` double DEFAULT NULL,
  `ContaNome` varchar(100) DEFAULT NULL,
  `Banco` varchar(50) DEFAULT NULL,
  `Agencia` varchar(25) DEFAULT NULL,
  `ContaNumero` varchar(25) DEFAULT NULL,
  `Documento` varchar(25) DEFAULT NULL,
  `RP` varchar(10) DEFAULT NULL,
  `Contrato` varchar(25) DEFAULT NULL,
  `Licitacao` varchar(50) DEFAULT NULL,
  `Historico` longtext,
  `CredorNoAtiva` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`idPagamento`),
  KEY `CNPJCPF` (`CNPJ-CPF`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador do credor (CNPJ ou CPF).',
  KEY `Unidade` (`Unidade`) COMMENT 'Permite busca, a ser realizada pelo Macros/Ativa, pelo identificador da Unidade.',
  KEY `DataPagamento` (`DataPagamento`) COMMENT 'Permitir consultas/ordenações mais rápidas pela data de pagamento. '
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_pagamentos`
--

/*!40000 ALTER TABLE `tcmba_pagamentos` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_pagamentos` ENABLE KEYS */;

--
-- Table structure for table `tcmba_unidades`
--

DROP TABLE IF EXISTS `tcmba_unidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tcmba_unidades` (
  `Codigo` int(11) NOT NULL AUTO_INCREMENT,
  `Descricao` varchar(75) DEFAULT NULL,
  `TipoUnidade` varchar(25) DEFAULT NULL,
  `Municipio` int(11) DEFAULT NULL,
  PRIMARY KEY (`Codigo`),
  KEY `Municipio` (`Municipio`) COMMENT 'Permitir consultas mais rápidas pelo código do Município. '
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tcmba_unidades`
--

/*!40000 ALTER TABLE `tcmba_unidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `tcmba_unidades` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-03-02 15:52:14
