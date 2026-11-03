# Graph Report - .  (2026-11-03)

## Corpus Check
- 19 files · ~58,845 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 206 nodes · 408 edges · 18 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `Bc()` - 16 edges
2. `Tween()` - 16 edges
3. `r()` - 13 edges
4. `s()` - 10 edges
5. `ja()` - 10 edges
6. `ka()` - 9 edges
7. `_d()` - 9 edges
8. `K()` - 8 edges
9. `t()` - 8 edges
10. `v()` - 8 edges

## Surprising Connections (you probably didn't know these)
- `P()` --calls--> `r()`  [EXTRACTED]
  assets/vendor/ScrollTrigger-3.12.5.min.js → assets/vendor/ScrollTrigger-3.12.5.min.js  _Bridges community 13 → community 6_
- `K()` --calls--> `z()`  [EXTRACTED]
  assets/vendor/ScrollTrigger-3.12.5.min.js → assets/vendor/ScrollTrigger-3.12.5.min.js  _Bridges community 9 → community 3_
- `Bc()` --calls--> `J()`  [EXTRACTED]
  assets/vendor/ScrollTrigger-3.12.5.min.js → assets/vendor/ScrollTrigger-3.12.5.min.js  _Bridges community 10 → community 3_
- `ff()` --calls--> `K()`  [EXTRACTED]
  assets/vendor/ScrollTrigger-3.12.5.min.js → assets/vendor/ScrollTrigger-3.12.5.min.js  _Bridges community 3 → community 6_
- `wc()` --calls--> `mb()`  [EXTRACTED]
  assets/vendor/ScrollTrigger-3.12.5.min.js → assets/vendor/ScrollTrigger-3.12.5.min.js  _Bridges community 10 → community 9_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (6): gc(), Ja(), Ka(), qb(), rb(), Sb()

### Community 1 - "Community 1"
Cohesion: 0.11
Nodes (28): _a(), ac(), _assertThisInitialized(), Co(), db(), ea(), eb(), fa() (+20 more)

### Community 2 - "Community 2"
Cohesion: 0.08
Nodes (4): ga(), ma(), na(), u()

### Community 3 - "Community 3"
Cohesion: 0.19
Nodes (14): A(), B(), Bc(), G(), Ia(), K(), ob(), rc() (+6 more)

### Community 4 - "Community 4"
Cohesion: 0.17
Nodes (3): cap(), chapter(), Builds the Wealth 360 client screening page from the Credit 360 screening page's

### Community 5 - "Community 5"
Cohesion: 0.22
Nodes (13): be(), _d(), ee(), ie(), je(), Kd(), ke(), Ld() (+5 more)

### Community 6 - "Community 6"
Cohesion: 0.26
Nodes (12): df(), ff(), gf(), hf(), jf(), M(), O(), of() (+4 more)

### Community 7 - "Community 7"
Cohesion: 0.29
Nodes (10): Ab(), Bb(), cb(), Context(), fb(), gb(), Gw(), t() (+2 more)

### Community 8 - "Community 8"
Cohesion: 0.36
Nodes (10): Aa(), Animation(), ha(), ia(), ja(), ka(), Ra(), Sa() (+2 more)

### Community 9 - "Community 9"
Cohesion: 0.36
Nodes (8): Db(), Jb(), La(), Ma(), Na(), Qa(), wc(), z()

### Community 10 - "Community 10"
Cohesion: 0.25
Nodes (8): Cb(), J(), mb(), mc(), oc(), Ta(), tb(), Ua()

### Community 11 - "Community 11"
Cohesion: 0.47
Nodes (3): digest(), mount(), sha256js()

### Community 12 - "Community 12"
Cohesion: 0.4
Nodes (5): le(), Ud(), vd(), wd(), yd()

### Community 13 - "Community 13"
Cohesion: 0.5
Nodes (4): N(), pc(), r(), sf()

### Community 14 - "Community 14"
Cohesion: 0.5
Nodes (4): tb(), Ub(), Vb(), za()

### Community 15 - "Community 15"
Cohesion: 0.5
Nodes (4): hb(), lb(), ob(), Wa()

### Community 16 - "Community 16"
Cohesion: 0.67
Nodes (3): Ec(), Fc(), MatchMedia()

### Community 17 - "Community 17"
Cohesion: 0.67
Nodes (3): Od(), Sd(), Td()

## Knowledge Gaps
- **1 isolated node(s):** `Builds the Wealth 360 client screening page from the Credit 360 screening page's`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Bc()` connect `Community 3` to `Community 0`, `Community 6`, `Community 9`, `Community 10`, `Community 13`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **Why does `Tween()` connect `Community 1` to `Community 8`, `Community 2`, `Community 7`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **Why does `r()` connect `Community 1` to `Community 2`, `Community 15`, `Community 7`?**
  _High betweenness centrality (0.001) - this node is a cross-community bridge._
- **What connects `Builds the Wealth 360 client screening page from the Credit 360 screening page's` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.06 - nodes in this community are weakly interconnected._
- **Should `Community 1` be split into smaller, more focused modules?**
  _Cohesion score 0.11 - nodes in this community are weakly interconnected._
- **Should `Community 2` be split into smaller, more focused modules?**
  _Cohesion score 0.08 - nodes in this community are weakly interconnected._