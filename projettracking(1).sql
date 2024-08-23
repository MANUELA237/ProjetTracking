-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : ven. 23 août 2024 à 20:04
-- Version du serveur :  10.4.18-MariaDB
-- Version de PHP : 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projettracking`
--

-- --------------------------------------------------------

--
-- Structure de la table `employes`
--

CREATE TABLE `employes` (
  `id` int(11) NOT NULL,
  `nom` varchar(120) NOT NULL,
  `email` varchar(120) NOT NULL,
  `poste` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `employes`
--

INSERT INTO `employes` (`id`, `nom`, `email`, `poste`) VALUES
(1, 'manou', 'yryiy@gmail.COM', 'comptable');

-- --------------------------------------------------------

--
-- Structure de la table `equipes`
--

CREATE TABLE `equipes` (
  `id` int(11) NOT NULL,
  `nom` varchar(120) NOT NULL,
  `specialite` varchar(200) NOT NULL,
  `employes` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `equipes`
--

INSERT INTO `equipes` (`id`, `nom`, `specialite`, `employes`) VALUES
(1, 'ff', 'gg', 'Jean Dupont');

-- --------------------------------------------------------

--
-- Structure de la table `projet`
--

CREATE TABLE `projet` (
  `id` int(11) NOT NULL,
  `nom` varchar(120) NOT NULL,
  `description` varchar(120) NOT NULL,
  `date_debut` varchar(200) NOT NULL,
  `date_fin` varchar(200) NOT NULL,
  `equipe` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `projet`
--

INSERT INTO `projet` (`id`, `nom`, `description`, `date_debut`, `date_fin`, `equipe`) VALUES
(1, 'fgg', 'eretrttt', '2024-08-22', '2024-08-29', 'Comptable'),
(2, 'peyebouo', 'gghhh', '2024-08-22', '2024-09-06', 'Développeur mobile');

-- --------------------------------------------------------

--
-- Structure de la table `taches`
--

CREATE TABLE `taches` (
  `id` int(11) NOT NULL,
  `nom` varchar(120) NOT NULL,
  `description` varchar(120) NOT NULL,
  `date_debut` varchar(200) NOT NULL,
  `date_fin` varchar(200) NOT NULL,
  `projet` varchar(200) NOT NULL,
  `employes` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `taches`
--

INSERT INTO `taches` (`id`, `nom`, `description`, `date_debut`, `date_fin`, `projet`, `employes`) VALUES
(1, 'manou', 'hgfdde', '2024-08-24', '2024-08-24', 'Développement d\'un logiciel de comptabilité', 'Sophie Durand');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `nom` varchar(120) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `user`
--

INSERT INTO `user` (`id`, `nom`, `email`, `password`) VALUES
(1, 'peyebouo', 'mabid@gmail.COM', '123'),
(2, 'gggg', 'rtyyu@gmail.COM', 'bbbbb'),
(3, 'manou', 'yryiy@gmail.COM', 'scrypt:32768:8:1$nN2uiTbM1pcHdUfw$fdb06a683ebee382217d289d864750dd11c8d213cd7523c43e4c0d8070809f40589cc9adc0f308f176966f35da34ad313d66d35cd12a67f55055e79f347e05aa'),
(4, 'CLYDE', 'clyde@gmail.com', 'scrypt:32768:8:1$b4wG7ytkLF8e5O8n$6388be40de8117b12beae3e9eb4fcda752af676c8220e5be414ff2e7d56d0ceb68f0fd0aff1507fce9dad0f9aca5f4f1763860ad8d65bc8d1fe7361e73e07f3c');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `employes`
--
ALTER TABLE `employes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `poste` (`poste`);

--
-- Index pour la table `equipes`
--
ALTER TABLE `equipes`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `projet`
--
ALTER TABLE `projet`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `taches`
--
ALTER TABLE `taches`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`);

--
-- Index pour la table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nom` (`nom`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `employes`
--
ALTER TABLE `employes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `equipes`
--
ALTER TABLE `equipes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `projet`
--
ALTER TABLE `projet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT pour la table `taches`
--
ALTER TABLE `taches`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT pour la table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
