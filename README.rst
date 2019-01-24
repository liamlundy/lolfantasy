League of Legends Fantasy
#########################

Installation
============

UNIX Systems (MacOS and Linux)
------------------------------

lolfantasy requires python 3.6 or higher. To install, navigate to the root
directory of this project and run:

.. code-block:: bash

    $ pip install .

Development
-----------

To install this project for development, navigate to the root directory and
run:

.. code-block:: bash

    $ pip install -e .

Usage
=====



Rules
=====

The Draft
---------

To build your dream team of LCS stars, you'll conduct a draft where you and
your competitors in your league take turns picking the players you want to form
your team.

You'll be picking the following positions:

  - 7 Starters:

    - 1 Top
    - 1 Jungler
    - 1 Mid
    - 1 AD Carry
    - 1 Support
    - 1 Flex player (an extra starter; can be a player from any position)
    - 1 Team (like Dignitas or Fnatic)
    - 3 Alternate players who can sub for a Starter

You can have a maximum of 2 players of the same position (you can't draft 3
Mids or 3 Teams). You'll earn points each week based on how well your Starters
do. See below for scoring details.

You have a minute to make each pick. The draft follows snake rules: each round,
the draft alternates pick order between first to last and last to first. To
learn more about the draft process before it starts, log in to your league and
check out our drafting tips to get acquainted with the draft screen. You can
also communicate a time when you want to start a draft with your league. Keep
in mind, you won't be able to start drafting until your league is filled up.

Scoring
-------

Each week, your team will be matched up against another team in your league.
Teams will earn points based on the performance of their starting line-up.
Alternates do not earn points.

LCS Players are scored accordingly:

  - 2 points per kill
  - -0.5 points per death
  - 1.5 points per assist
  - 0.01 points per creep kill
  - 2 points for a triple kill
  - 5 points for a quadra kill (doesn't also count as a triple kill)
  - 10 points for a penta kill (doesn't also count as a quadra kill)
  - 2 points if a player attains 10 or more assists or kills in a game (this
    bonus only applies once)

LCS Teams are scored accordingly:

  - 2 points per win
  - 2 points per Baron Nashor killed
  - 1 point per Dragon killed
  - 2 points per First Blood earned
  - 1 point per Tower destroyed
  - 2 points if the team wins in less than 30 minutes
