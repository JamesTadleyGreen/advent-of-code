module Main where

import Criterion.Main
import Days.Day01
import Days.Day02
import Days.Day03
import Days.Day04
import Days.Day05
import Days.Day06

main :: IO ()
-- main = defaultMain [bench "test" $ nfIO (print day06)]
main = print day06
