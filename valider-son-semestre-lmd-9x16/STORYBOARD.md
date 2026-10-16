---
format: 1080x1920
duration: 90s
message: "Tu valides ton semestre avec des crédits, pas matière par matière."
arc: story-explainer with how-to
audience: "Étudiants de L1, toutes filières, UASZ"
mode: collaborative
language: fr
music: calm optimistic minimal piano underscore, educational, unobtrusive
---

# Comment valider ton semestre — Storyboard

## Video direction

- palette: frame.md Blue Professional — fond crème #fdfae7, cobalt #1e2bfa seul accent (chiffres, eyebrows, barres), titres quasi-noirs, rouge #dc2626 = UE sous 10, vert #059669 = validé. Rien d'autre.
- motion grammar: entrées `fromTo` sur courbes longues (power3.out par défaut), aucune entrée rebondissante sauf le tampon « Semestre validé » et le cadenas (spring-pop-entrance). Chaque élément apparaît quand la voix le nomme ; jamais de canevas complet à t=0. Pas de sortie (la transition racine sert de sortie) sauf la frame 8.
- held frames: frame 5 (après le tampon, tenue immobile ~2 s — climax) et frame 8 (lecture finale + source). Tenue = immobilité, pas de respiration.
- negative list: pas de dégradé violet « IA », pas de bokeh, pas d'ombres, pas de logo UASZ inventé ; ni diaporama (tout d'un coup puis figé) ni économiseur d'écran (tout qui flotte).
- texte à l'écran: mots-clés et chiffres uniquement — les phrases de la voix passent par les sous-titres.

Stage commun : un **relevé de notes stylisé d'Awa** (4 cartes UE) qui reste le même objet d'un bout à l'autre — il se découpe, se calcule, se verrouille. Aucun logo UASZ inventé ; seul le texte « UASZ » apparaît. Source affichée en fin de capsule.

## Frame 1 — Le faux échec

- scene: Relevé d'Awa (S1) apparaît ; le 8,5 d'une UE vire au rouge, puis un « Raté ? » se barre et devient « Faux. »
- voiceover: "Voici Awa, en L1 à l'UASZ. Résultats du semestre 1 : 8,5 dans une UE. Elle croit avoir raté son semestre. Elle a tort."
- duration: 11.546s
- transition_in: cut
- status: animated
- src: compositions/frames/01-faux-echec.html
- type: hook
- persuasion: Common-belief vs reality + Direct address (persona)
- beat: Recognition + surprise
- blueprint: kinetic-type-beats (Adapt)
- focal: le 8,5 rouge du relevé
- roles: relevé = foreground subject · « Raté ? / Faux. » = supporting type · fond crème = background

narrativeRole: Ouvre l'écart cognitif sur la croyance la plus répandue chez les L1 : « une note sous 10 = semestre raté ».
keyMessage: Une UE sous 10 ne signifie pas que le semestre est perdu.

Scene 1 (0.0–2.0s): étiquette « Awa · L1 · UASZ » + carte relevé glissent (fromTo y/opacity), split 45/55.
Scene 2 (2.0–5.0s): les 4 lignes UE entrent en cascade ; à ~4 s la ligne UE 2 (8,5) s'encadre de rouge.
Scene 3 (5.0–7.4s): « Raté ? » apparaît en gris.
Scene 4 (7.4–10s): un trait rouge barre « Raté ? » (scaleX), « Faux. » arrive (per-word reveal) et tient.

## Frame 2 — UE et crédits

- scene: La barre du semestre (30 crédits) se découpe en 4 blocs UE de tailles proportionnelles (9 · 9 · 6 · 6), chacun étiqueté « UE » + crédits ; compteur 0 → 30.
- voiceover: "Ton semestre est découpé en unités d'enseignement : les UE. Chaque UE vaut des crédits, et un semestre en compte 30."
- duration: 8.333s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-ue-credits.html
- type: product_intro
- persuasion: Frame-then-fill + Progressive disclosure
- beat: Orientation + clarity
- blueprint: grid-card-assemble (Adapt)
- focal: la barre de 30 crédits découpée en 4 UE
- roles: blocs UE = foreground subject · titre = supporting · axe 0→30 = supporting

narrativeRole: Pose le vocabulaire et l'unité de compte — l'UE et le crédit — sur le stage qui servira tout le film.
keyMessage: Un semestre = 30 crédits répartis entre des UE.

Scene 1 (0.0–2.5s): titre « Un semestre = … crédits » entre ; libellé « UE = unité d'enseignement ».
Scene 2 (2.5–5.0s): les 4 blocs UE s'assemblent de gauche à droite (waterfall-entry), largeurs ∝ crédits.
Scene 3 (5.0–7.0s): les nombres de crédits 9 · 9 · 6 · 6 apparaissent dans chaque bloc.
Scene 4 (7.0–10s): le « 30 » du titre compte 0→30 (counting-dynamic-scale), l'axe s'affiche ; tenue.

## Frame 3 — Valider une UE

- scene: Zoom sur une carte UE : seuil 10/20 en ligne horizontale ; deux matières (7 et 13) se rejoignent en une moyenne 10 qui franchit le seuil → coche verte.
- voiceover: "Une UE est validée à partir de 10 sur 20. À l'intérieur d'une UE, tes matières se compensent entre elles."
- duration: 7.837s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/03-valider-ue.html
- type: feature_showcase
- persuasion: Demonstration + Worked example with real numbers
- beat: Comprehension
- blueprint: dataviz-countup (Adapt)
- focal: le seuil 10/20 et la moyenne d'UE qui l'atteint
- roles: carte UE 3 = foreground subject · libellés droite = supporting

narrativeRole: Premier niveau du mécanisme : la règle des 10/20 et la compensation interne à une UE.
keyMessage: Une UE se valide à 10/20, et ses matières se compensent entre elles.

Scene 1 (0.0–2.5s): titre « Une UE est validée à 10/20 », « 10/20 » pop discret.
Scene 2 (2.5–5.5s): carte UE 3 entre ; Matière A (7, rouge) puis Matière B (13).
Scene 3 (5.5–8.0s): libellés « Compensation entre matières » à droite ; la moyenne compte 0→10.
Scene 4 (8.0–10s): pastille « Validée » (spring-pop) ; tenue.

## Frame 4 — La compensation entre UE

- scene: Retour au relevé complet ; l'UE à 8,5 reste rouge ; les 4 UE glissent dans une « balance » pondérée où chaque bloc a le poids de ses crédits.
- voiceover: "Et si une UE est sous la moyenne ? C'est là qu'intervient la compensation : on calcule ta moyenne sur l'ensemble des UE, chacune pondérée par ses crédits."
- duration: 10.736s
- transition_in: zoom-through
- status: animated
- src: compositions/frames/04-compensation.html
- type: feature_showcase
- persuasion: Question→answer pairing + Concretization (balance pondérée)
- beat: "Aha" + anticipation
- blueprint: kinetic-type-beats (Adapt)
- focal: les 4 UE posées sur la balance pondérée
- roles: blocs UE (hauteur ∝ crédits) = foreground subject · fléau + pivot = supporting

narrativeRole: Nomme et explique la compensation intra-semestre — le cœur de la capsule.
keyMessage: Le semestre se juge sur la moyenne des UE pondérée par leurs crédits.

Scene 1 (0.0–3.0s): question « Et si une UE est sous la moyenne ? » révélée mot à mot.
Scene 2 (3.0–5.0s): libellé « Moyenne pondérée par les crédits ».
Scene 3 (5.0–7.5s): les 4 blocs montent en cascade, UE 2 et UE 4 bordées de rouge.
Scene 4 (7.5–12s): fléau + pivot apparaissent ; étiquettes « poids 9 / 6 » s'allument au mot « pondérée » ; tenue.

## Frame 5 — Le calcul d'Awa

- scene: Le calcul s'écrit terme à terme sous les 4 cartes (12×9 + 8,5×9 + 11×6 + 9×6) ÷ 30 ; compteur 0 → 10,15 ; tampon « Semestre validé · 30 crédits ».
- voiceover: "Awa : 12, 8,5, 11 et 9. Moyenne : 10,15. Semestre validé, 30 crédits acquis."
- duration: 12.1s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-calcul-awa.html
- type: social_proof
- persuasion: Worked example with real numbers + Callback (le 8,5 du hook)
- beat: Delight + "now I get it"
- blueprint: dataviz-countup (Adapt)
- focal: le compteur 10,15
- roles: compteur = foreground subject · cartes notes + formule = supporting · tampon = payoff

narrativeRole: Résout le cas du hook avec le calcul réel ; le compteur est le moment fort.
keyMessage: Avec 8,5 dans une UE, Awa valide quand même : 10,15 de moyenne pondérée.

Scene 1 (0.0–3.0s): les 4 cartes entrent une à une sur l'énumération « 12, 8,5, 11 et 9 ».
Scene 2 (3.0–4.5s): la formule s'écrit terme à terme.
Scene 3 (4.5–7.0s): compteur 0 → 10,15 avec croissance d'échelle (counting-dynamic-scale).
Scene 4 (7.0–11s): tampon « Semestre validé · 30 crédits acquis » claque (spring-pop) ; tenue immobile (climax).

## Frame 6 — La capitalisation

- scene: Variante : un autre relevé où le semestre n'est pas validé ; les UE ≥ 10 se verrouillent d'un cadenas et restent allumées ; mot-titre « Capitalisation ».
- voiceover: "Et si ça ne passe pas ? Chaque UE validée reste acquise à vie, avec ses crédits. C'est la capitalisation."
- duration: 8.751s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-capitalisation.html
- type: feature_showcase
- persuasion: Counterexample + Coined term
- beat: Reassurance + confidence
- blueprint: kinetic-type-beats (Adapt)
- focal: les cadenas sur les UE validées
- roles: cartes UE = foreground subject · cadenas = payoff · titre « capitalisation » = coined term

narrativeRole: Couvre le cas d'échec et rassure : rien de validé n'est perdu.
keyMessage: Une UE validée est acquise définitivement, avec ses crédits.

Scene 1 (0.0–2.0s): les 4 cartes de l'exemple entrent (estompées), mention « moyenne 9,4 → non validé ».
Scene 2 (2.0–5.5s): UE 1 puis UE 3 s'allument et leurs cadenas tombent (spring-pop).
Scene 3 (5.5–7.0s): « 15 crédits acquis à vie » apparaît.
Scene 4 (7.0–10s): le titre « La capitalisation » arrive au mot prononcé ; tenue.

## Frame 7 — Passer en L2

- scene: Jauge horizontale de 60 crédits (S1 + S2) ; repère à 70 % = 42 crédits ; la jauge se remplit jusqu'au repère → étiquette « Passage conditionnel en L2 ».
- voiceover: "Bon à savoir : avec au moins 42 crédits sur les 60 de L1, tu peux passer en L2 sous condition."
- duration: 7.889s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-passage-l2.html
- type: benefit_highlight
- persuasion: Anchoring on a familiar referent (jauge) + Statistical proof
- beat: Foresight
- blueprint: dataviz-countup (Adapt)
- focal: la jauge qui se remplit jusqu'à 42
- roles: jauge 60 crédits = foreground subject · repère 70 % = supporting · pastille = payoff

narrativeRole: Élargit du semestre à l'année : la conséquence concrète des crédits capitalisés.
keyMessage: 42 crédits sur 60 en L1 ouvrent le passage conditionnel en L2.

Scene 1 (0.0–2.5s): titre ; piste de jauge vide + libellés Semestre 1 / Semestre 2.
Scene 2 (2.5–4.8s): le « 42 » compte, la jauge se remplit jusqu'à 70 % (stat-bars-and-fills).
Scene 3 (4.8–6.5s): repère vertical + « 70 % = 42 crédits ».
Scene 4 (6.5–9s): pastille « Passage conditionnel en L2 » ; tenue.

## Frame 8 — À retenir

- scene: Trois tuiles s'empilent : « 10 de moyenne pondérée » · « 30 crédits » · « Acquis à vie » ; bandeau final « Décret n° 2012-1114, art. 9, 27–29 » + « UASZ · Direction de la scolarité ».
- voiceover: "À retenir : 10 de moyenne pondérée, 30 crédits, et tout ce qui est validé reste acquis."
- duration: 10s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-a-retenir.html
- type: branding
- persuasion: Distillation + Rule of three + Citation / source
- beat: Satisfaction + resolve
- blueprint: grid-card-assemble (Adapt)
- focal: les trois tuiles à retenir
- roles: tuiles = foreground subject (triptyque) · source + signature = supporting

narrativeRole: Condense la capsule en trois repères mémorisables et ancre la légitimité réglementaire.
keyMessage: 10 de moyenne pondérée, 30 crédits, acquis à vie — décret 2012-1114.

Scene 1 (0.0–2.6s): eyebrow ; tuile « 10 » entre.
Scene 2 (2.6–4.6s): tuile « 30 » entre.
Scene 3 (4.6–7.0s): tuile « À vie » entre.
Scene 4 (7.0–10s): source « Décret n° 2012-1114… » + signature UASZ ; tenue jusqu'à la fin (frame finale).

