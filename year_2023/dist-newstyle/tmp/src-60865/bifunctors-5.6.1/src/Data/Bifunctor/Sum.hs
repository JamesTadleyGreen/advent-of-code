{-# LANGUAGE DeriveFoldable #-}
{-# LANGUAGE DeriveFunctor #-}
{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE DeriveTraversable #-}
{-# LANGUAGE EmptyDataDecls #-}
{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE PolyKinds #-}
{-# LANGUAGE Safe #-}
{-# LANGUAGE StandaloneDeriving #-}
{-# LANGUAGE TypeFamilies #-}

module Data.Bifunctor.Sum where

import Data.Bifunctor
import Data.Bifunctor.Functor
import Data.Bifunctor.Swap (Swap (..))
import Data.Bifoldable
import Data.Bitraversable
import Data.Functor.Classes
import GHC.Generics

data Sum p q a b = L2 (p a b) | R2 (q a b)
  deriving (Eq, Ord, Show, Read, Generic, Generic1)
deriving instance (Functor (f a), Functor (g a)) => Functor (Sum f g a)
deriving instance (Foldable (f a), Foldable (g a)) => Foldable (Sum f g a)
deriving instance (Traversable (f a), Traversable (g a)) => Traversable (Sum f g a)

instance (Eq2 f, Eq2 g, Eq a) => Eq1 (Sum f g a) where
  liftEq = liftEq2 (==)
instance (Eq2 f, Eq2 g) => Eq2 (Sum f g) where
  liftEq2 f g (L2 x1) (L2 x2) = liftEq2 f g x1 x2
  liftEq2 _ _ (L2 _)  (R2 _)  = False
  liftEq2 _ _ (R2 _)  (L2 _)  = False
  liftEq2 f g (R2 y1) (R2 y2) = liftEq2 f g y1 y2

instance (Ord2 f, Ord2 g, Ord a) => Ord1 (Sum f g a) where
  liftCompare = liftCompare2 compare
instance (Ord2 f, Ord2 g) => Ord2 (Sum f g) where
  liftCompare2 f g (L2 x1) (L2 x2) = liftCompare2 f g x1 x2
  liftCompare2 _ _ (L2 _)  (R2 _)  = LT
  liftCompare2 _ _ (R2 _)  (L2 _)  = GT
  liftCompare2 f g (R2 y1) (R2 y2) = liftCompare2 f g y1 y2

instance (Read2 f, Read2 g, Read a) => Read1 (Sum f g a) where
  liftReadsPrec = liftReadsPrec2 readsPrec readList
instance (Read2 f, Read2 g) => Read2 (Sum f g) where
  liftReadsPrec2 rp1 rl1 rp2 rl2 = readsData $
    readsUnaryWith (liftReadsPrec2 rp1 rl1 rp2 rl2) "L2" L2 `mappend`
    readsUnaryWith (liftReadsPrec2 rp1 rl1 rp2 rl2) "R2" R2

instance (Show2 f, Show2 g, Show a) => Show1 (Sum f g a) where
  liftShowsPrec = liftShowsPrec2 showsPrec showList
instance (Show2 f, Show2 g) => Show2 (Sum f g) where
  liftShowsPrec2 sp1 sl1 sp2 sl2 p (L2 x) =
    showsUnaryWith (liftShowsPrec2 sp1 sl1 sp2 sl2) "L2" p x
  liftShowsPrec2 sp1 sl1 sp2 sl2 p (R2 y) =
    showsUnaryWith (liftShowsPrec2 sp1 sl1 sp2 sl2) "R2" p y

instance (Bifunctor p, Bifunctor q) => Bifunctor (Sum p q) where
  bimap f g (L2 p) = L2 (bimap f g p)
  bimap f g (R2 q) = R2 (bimap f g q)
  first f (L2 p) = L2 (first f p)
  first f (R2 q) = R2 (first f q)
  second f (L2 p) = L2 (second f p)
  second f (R2 q) = R2 (second f q)

instance (Bifoldable p, Bifoldable q) => Bifoldable (Sum p q) where
  bifoldMap f g (L2 p) = bifoldMap f g p
  bifoldMap f g (R2 q) = bifoldMap f g q

instance (Bitraversable p, Bitraversable q) => Bitraversable (Sum p q) where
  bitraverse f g (L2 p) = L2 <$> bitraverse f g p
  bitraverse f g (R2 q) = R2 <$> bitraverse f g q

instance BifunctorFunctor (Sum p) where
  bifmap _ (L2 p) = L2 p
  bifmap f (R2 q) = R2 (f q)

instance BifunctorMonad (Sum p) where
  bireturn = R2
  bijoin (L2 p) = L2 p
  bijoin (R2 q) = q
  bibind _ (L2 p) = L2 p
  bibind f (R2 q) = f q

-- | @since 5.6.1
instance (Swap p, Swap q) => Swap (Sum p q) where
  swap (L2 p) = L2 (swap p)
  swap (R2 q) = R2 (swap q)
