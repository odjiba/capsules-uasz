---
workflow: faceless-explainer
flow: automation
storyboard: yes
message: "Tu valides ton semestre avec des crédits, pas matière par matière."
destination: website
aspect: 1080x1920
language: fr
audience: "Étudiants de Licence 1, toutes filières, Université Assane Seck de Ziguinchor (UASZ)"
length: 90s
angle: how-to
---

## Intent

Capsule pédagogique officielle de la Direction de la scolarité centrale de l'UASZ.
Cas pratique : on suit Awa, étudiante en L1, de son relevé de notes du semestre 1
jusqu'au verdict « semestre validé ». Objectif d'apprentissage : l'étudiant sera
capable de **déterminer** s'il valide son semestre à partir de ses notes d'UE.
Ton : clair, rassurant, institutionnel mais accessible aux L1.

Script validé par l'utilisateur (script v0) — à utiliser tel quel (VO_MODE: verbatim).

## Customizations

- Count-up animé sur la moyenne pondérée (10,15) — moment fort.
- Calcul pondéré animé : (12×9 + 8,5×9 + 11×6 + 9×6) ÷ 30 = 10,15.
- Cadenas sur les UE capitalisées ; jauge 60 crédits avec repère 70 % (42 crédits).
- Sous-titres incrustés (visionnage sans son).
- Musique de fond discrète, abaissée sous la voix.
- Voix : synthèse HeyGen, français (bloquée tant que api.heygen.com n'est pas autorisé dans le réseau de l'environnement).
- Déclinaison 9:16 (1080x1920) à produire APRÈS le master 16:9 : une info par écran, pas de simple recadrage.

## Notes

- Source réglementaire UNIQUE : Décret n° 2012-1114 du 12 octobre 2012 relatif au diplôme de licence (art. 3, 9, 26-29). Citer « Décret n° 2012-1114, art. 9, 27–29 » à l'écran en fin de capsule.
- NE PAS mentionner de note éliminatoire ni de compensation annuelle entre semestres : non prévues par le décret (décision utilisateur : on s'en tient au décret).
- Simplifications assumées : pas de mention de la reprise d'UE dans un semestre non validé (art. 28) ni de la conservation des notes ≥10 pour le rattrapage (art. 27).
- Design system proposé par Claude, conçu pour être remplacé en une passe par la charte officielle UASZ (logo + couleurs) quand l'utilisateur la fournira. Ne pas inventer de logo UASZ.
- Prénom du personnage : Awa (validé).
