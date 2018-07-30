-- phpMyAdmin SQL Dump
-- version 4.8.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Jul 2018 pada 00.39
-- Versi server: 10.1.33-MariaDB
-- Versi PHP: 7.2.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_saw_python`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `alternatif`
--

CREATE TABLE `alternatif` (
  `id_alternatif` int(11) NOT NULL,
  `nama_alternatif` varchar(200) DEFAULT NULL,
  `deskripsi` text
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `alternatif`
--

INSERT INTO `alternatif` (`id_alternatif`, `nama_alternatif`, `deskripsi`) VALUES
(1, 'Galaxy', 'Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy \r\n\r\nGalaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy Galaxy '),
(2, 'Iphone', 'Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone \r\n\r\nIphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone Iphone '),
(3, 'BB', 'BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB \r\n\r\nBB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB BB '),
(4, 'Lumia', 'Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia \r\n\r\nLumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia Lumia ');

-- --------------------------------------------------------

--
-- Struktur dari tabel `alternatif_kriteria`
--

CREATE TABLE `alternatif_kriteria` (
  `id_alternatif_kriteria` int(11) NOT NULL,
  `id_alternatif` int(11) DEFAULT NULL,
  `id_kriteria` int(11) DEFAULT NULL,
  `nilai` double DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `alternatif_kriteria`
--

INSERT INTO `alternatif_kriteria` (`id_alternatif_kriteria`, `id_alternatif`, `id_kriteria`, `nilai`) VALUES
(1, 1, 1, 3500),
(2, 1, 2, 70),
(3, 1, 3, 10),
(4, 1, 4, 80),
(5, 1, 5, 3000),
(6, 1, 6, 36),
(7, 2, 1, 4500),
(8, 2, 2, 90),
(9, 2, 3, 10),
(10, 2, 4, 60),
(11, 2, 5, 2500),
(12, 2, 6, 48),
(13, 3, 1, 4000),
(14, 3, 2, 80),
(15, 3, 3, 9),
(16, 3, 4, 90),
(17, 3, 5, 2000),
(18, 3, 6, 48),
(19, 4, 1, 4000),
(20, 4, 2, 70),
(21, 4, 3, 8),
(22, 4, 4, 50),
(23, 4, 5, 1500),
(24, 4, 6, 60);

-- --------------------------------------------------------

--
-- Struktur dari tabel `kriteria`
--

CREATE TABLE `kriteria` (
  `id_kriteria` int(11) NOT NULL,
  `nama_kriteria` varchar(100) DEFAULT NULL,
  `kepentingan` double DEFAULT NULL,
  `costbenefit` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `kriteria`
--

INSERT INTO `kriteria` (`id_kriteria`, `nama_kriteria`, `kepentingan`, `costbenefit`) VALUES
(1, 'Harga', 0.2, 'cost'),
(2, 'Kualitas', 0.25, 'benefit'),
(3, 'Fitur', 0.2, 'benefit'),
(4, 'Populer', 0.125, 'benefit'),
(5, 'Purna Jual', 0.125, 'benefit'),
(6, 'Keawetan', 0.1, 'benefit');

-- --------------------------------------------------------

--
-- Struktur dari tabel `login`
--

CREATE TABLE `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `login`
--

INSERT INTO `login` (`username`, `password`) VALUES
('admin', '123');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `alternatif`
--
ALTER TABLE `alternatif`
  ADD PRIMARY KEY (`id_alternatif`);

--
-- Indeks untuk tabel `alternatif_kriteria`
--
ALTER TABLE `alternatif_kriteria`
  ADD PRIMARY KEY (`id_alternatif_kriteria`);

--
-- Indeks untuk tabel `kriteria`
--
ALTER TABLE `kriteria`
  ADD PRIMARY KEY (`id_kriteria`);

--
-- Indeks untuk tabel `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`username`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `alternatif`
--
ALTER TABLE `alternatif`
  MODIFY `id_alternatif` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT untuk tabel `alternatif_kriteria`
--
ALTER TABLE `alternatif_kriteria`
  MODIFY `id_alternatif_kriteria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT untuk tabel `kriteria`
--
ALTER TABLE `kriteria`
  MODIFY `id_kriteria` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
