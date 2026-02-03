#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de génération du PDF complet : Hypnomachie - Le Combat contre l'Hypnose Sociale
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Contenu complet du document
TITRE_PRINCIPAL = "HYPNOMACHIE"
SOUS_TITRE = "Le Combat contre l'Hypnose Sociale"
AUTEUR = "Reformulation intégrale de l'entretien Frédéric Bascunana / Bascar"
PARTIE = "Partie 2 : Le ruissellement de la perversion"

# Chapitres avec leur contenu
CHAPITRES = [
    {
        "titre": "PRÉAMBULE",
        "contenu": """Ce document est une reformulation directe, sans langue de bois ni filtre idéologique, d'un entretien de 3h30 entre Frédéric Bascunana (chaîne Parisiste/Paris Intelligence Collective) et Bascar (chaîne Hypnomachie), avec les interventions d'Alain Gonzalez. L'objectif est de restituer fidèlement la substance des propos tenus, sans édulcoration."""
    },
    {
        "titre": "CHAPITRE 1 : L'HYPNOMACHIE ET LA NATURE DE L'HYPNOSE SOCIALE",
        "sections": [
            {
                "sous_titre": "Le combat contre le sommeil collectif",
                "texte": """Hypnomachie. Ce mot, forgé sur le modèle de tauromachie, désigne littéralement le combat contre l'hypnose. Mais de quelle hypnose parle-t-on exactement ? Certainement pas de celle des spectacles de music-hall où un bonimenteur fait aboyer des volontaires devant un public hilare. Non, il s'agit d'une hypnose bien plus profonde, bien plus insidieuse, et surtout bien plus répandue : celle dans laquelle baigne l'immense majorité de la population sans même s'en rendre compte.

La thèse centrale est brutale dans sa simplicité : les êtres humains passent l'essentiel de leur vie dans un état de conscience modifié proche de la transe. Ce n'est pas une métaphore poétique pour dire que les gens sont distraits ou inattentifs. C'est un constat clinique, observable, mesurable. Les gens étaient déjà peu attentifs dans les années soixante-dix et quatre-vingt, mais l'ajout d'un smartphone et d'écouteurs n'a certainement pas arrangé les choses.

Quiconque a pratiqué un peu de close-up, cette magie à courte distance qui repose sur le détournement de l'attention, sait à quel point il est facile de manipuler la perception d'autrui. Les pickpockets le savent aussi. Les politiciens également. Tous exploitent le même phénomène fondamental : les gens sont naturellement, structurellement, dans un état de conscience modifié qui les rend vulnérables à l'influence."""
            },
            {
                "sous_titre": "La preuve par l'expérience",
                "texte": """Il existe un test simple, à la portée de tous, pour démontrer cette réalité. Prenez conscience maintenant de votre cuisse et de votre genou droit. Sentez les muscles, la rotule, cette légère pulsation si vous êtes suffisamment attentif. Maintenant, essayez de maintenir cette sensation pendant que vous continuez à lire, pendant une demi-heure, une heure.

L'immense majorité des personnes non entraînées sont totalement incapables de conserver cette sensation pendant ne serait-ce que cinq minutes. Or c'est notre propre corps. N'importe quel mammifère devrait pouvoir faire cela naturellement. Mais nous, nous en sommes incapables. Pourquoi ? Parce que nous sommes en transe.

Cette simple expérience devrait faire réfléchir tous ceux qui affirment avec assurance qu'ils ne sont pas hypnotisables, qu'ils sont parfaitement éveillés et maîtres de leurs choix."""
            },
            {
                "sous_titre": "Au-delà de la transe : existe-t-il autre chose ?",
                "texte": """La question fondamentale qui se pose alors est celle-ci : n'existe-t-il que la transe ? Les hypnothérapeutes eux-mêmes affirment souvent qu'on ne fait que passer d'une transe à une autre. Cette vision est séduisante dans sa cohérence, mais elle est incomplète.

Il existe autre chose. Il existe des états de conscience qui ne sont ni dissociatifs ni identificatoires, qui ne relèvent ni de la focalisation excessive ni de l'expansion incontrôlée. Mais atteindre ces états demande un travail, une dépense d'énergie, ce que l'on pourrait appeler un coût d'entrée."""
            },
            {
                "sous_titre": "Le langage comme produit de l'hypnose",
                "texte": """Un obstacle fondamental se dresse sur le chemin de quiconque tente de définir l'hypnose avec précision : le langage lui-même. Définir l'hypnose de façon rationnelle, carrée, scientifique, est un échec cuisant. Beaucoup ont essayé, tous ont échoué. La raison en est profonde : rien ne nous dit que le langage n'est pas lui-même un sous-produit de l'hypnose.

Nous voilà face à ce qu'on peut appeler une parachosmie, une situation où deux notions théoriques tentent de se phagocyter mutuellement, comme deux serpents qui essaieraient chacun d'avaler l'autre."""
            },
            {
                "sous_titre": "Focalisation et expansion : les deux pôles de la transe",
                "texte": """Une erreur courante consiste à réduire l'hypnose à la focalisation de l'attention. On a vu cela pendant la crise Covid : les gens étaient tellement focalisés sur le nombre de cas, sur les débats autour du masque, qu'ils ne voyaient plus les effets pervers à côté, les dépressions, les faillites, la maltraitance des enfants confinés.

Cette capacité du pouvoir à braquer un projecteur sur un point minuscule pour plonger tout le reste de la réalité dans le noir absolu existe bel et bien. Mais il existe aussi des transes hypnotiques qui relèvent au contraire de l'expansion, de l'hyper-sensibilité."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 2 : LA NÉOTÉNIE HUMAINE ET LE TRAUMA COMME NORME",
        "sections": [
            {
                "sous_titre": "Une espèce qui naît inachevée",
                "texte": """L'être humain est une espèce néoténique. Ce terme technique désigne une réalité simple mais aux conséquences profondes : nous naissons inachevés. Notre gestation utérine est relativement courte par rapport à notre développement global, ce qui signifie que nous arrivons au monde dans un état de fragilité extrême.

Prenez un girafon. Quelques heures après sa naissance, il est déjà capable de marcher, de courir, de fuir un éventuel prédateur. Un bébé humain au bout de six heures ? Il est à peine capable de tourner la tête. Cette néoténie implique une gestation extra-utérine qui, selon les psychologues, dure entre trente et trente-cinq ans."""
            },
            {
                "sous_titre": "Les parents comme premiers hypnotiseurs",
                "texte": """Dans ce contexte de fragilité prolongée, les parents jouent un rôle déterminant. Mais voici le problème : la plupart des parents sont eux-mêmes des êtres traumatisés, élevés par des parents eux-mêmes traumatisés, dans une chaîne de transmission qui remonte à la nuit des temps.

Les parents normaux, ceux qui font leurs trente-huit heures, qui galèrent pour boucler leurs fins de mois, ne peuvent tout simplement pas faire correctement le travail d'élever un enfant. L'enfant se retrouve donc livré à lui-même avec un système nerveux qui n'est pas à la hauteur du monde qui l'entoure."""
            },
            {
                "sous_titre": "Il n'y a pas d'hétéro-hypnose",
                "texte": """Un point fondamental doit être compris : il n'y a pas véritablement d'hétéro-hypnose. Personne ne peut hypnotiser quelqu'un qui n'a pas des prédispositions et une envie, même inconsciente, d'entrer en transe. C'est toujours l'individu lui-même qui entre en transe, l'hypnotiseur ne fait que guider ce processus.

Les enfants sont des machines à s'auto-hypnotiser. Montrez-leur des nuages et ils y verront des éléphants, des dragons, des châteaux. Cette capacité extraordinaire à entrer en transe est naturelle chez l'enfant, elle fait partie de son développement normal."""
            },
            {
                "sous_titre": "Le deep mama",
                "texte": """C'est ce qu'un ami a brillamment résumé par l'expression "deep mama", en écho au "deep state". Nous sommes gouvernés par une mafia qui exploite nos pulsions régressives, notre désir de retourner dans l'utérus maternel, notre refus d'assumer les responsabilités de l'âge adulte.

Cette deep mama ne nous impose pas la régression par la force. Elle exploite notre propre désir de régression, notre propre peur de la liberté et de la responsabilité."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 3 : DISSOCIATION ET IDENTIFICATION - LES DEUX FACES DE LA TRANSE",
        "sections": [
            {
                "sous_titre": "Le piège de la définition unique",
                "texte": """Une erreur fondamentale consiste à réduire l'hypnose à la seule dissociation. La dissociation est effectivement une forme de transe hypnotique. Mais ce qu'on oublie généralement de préciser, c'est que le contraire de la dissociation, à savoir l'identification, est tout autant une transe hypnotique. Ce sont les deux faces d'une même pièce."""
            },
            {
                "sous_titre": "L'identification comme transe",
                "texte": """Quand quelqu'un dit "je suis boulanger", "je suis professeur des écoles", "je suis agrégé en lettres", il est en pleine transe identificatoire. Non, tu n'ES pas boulanger. Tu exerces le métier de boulanger. Tu AS un diplôme d'agrégation. Mais tu n'ES pas ces choses. Cette confusion entre être et avoir, entre identité profonde et rôle social, est caractéristique de l'état de transe."""
            },
            {
                "sous_titre": "Les transes guerrières",
                "texte": """Pour comprendre que l'identification est bien une forme de transe, il suffit de regarder les exemples extrêmes. En Indonésie, dans certaines traditions, des hommes entrent dans des transes où ils se lacèrent le dos à la machette, se plantent des piques dans la gorge. Ces transes guerrières sont des transes d'identification extrême. On retrouve le même phénomène dans le vaudou haïtien, chez les Vikings avec la Sömaféra."""
            },
            {
                "sous_titre": "L'avatarisation de soi",
                "texte": """Cette dissociation est amplifiée par le monde numérique contemporain. Nous vivons désormais avec un nombre excessif d'avatars. Des femmes utilisent TikTok avec des filtres qui les embellissent de manière spectaculaire. Elles finissent par devenir l'ombre de leur propre moi numérique.

C'est exactement le projet décrit par Klaus Schwab : la fusion des identités biologiques, numériques et sociales. D'abord segmenter l'identité en fragments séparés, puis rerassembler ces fragments sous une forme nouvelle, contrôlable."""
            },
            {
                "sous_titre": "Le troisième terme",
                "texte": """L'objectif de tout travail véritable sur soi n'est pas de passer de la dissociation à l'identification ou inversement. L'objectif est de trouver un troisième terme, un état de conscience qui n'est ni dissocié ni identifié. Cet état existe. Il peut être expérimenté. Mais il demande un travail considérable pour être atteint."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 4 : LE COVID COMME LABORATOIRE D'HYPNOSE SOCIALE",
        "sections": [
            {
                "sous_titre": "La formation de masse",
                "texte": """La période Covid a constitué un laboratoire à ciel ouvert pour observer les mécanismes de l'hypnose sociale à grande échelle. Le psychologue belge Mattias Desmet a proposé le concept de "formation de masse" pour décrire ce phénomène.

Cette formation de masse présente des caractéristiques bien identifiées. Elle surgit dans des sociétés où un grand nombre de personnes souffrent d'un manque de sens, d'une anxiété flottante sans objet précis. Quand un narratif apparaît qui donne soudain un sens à cette anxiété, une partie significative de la population s'y accroche avec une ferveur quasi religieuse."""
            },
            {
                "sous_titre": "L'auto-attestation comme rituel",
                "texte": """L'auto-attestation de sortie mérite une analyse approfondie car elle concentre en elle plusieurs mécanismes hypnotiques. En apparence, c'était une simple formalité administrative. En réalité, c'était un rituel de soumission qui activait des ressorts psychologiques profonds.

D'abord, le simple fait de devoir demander la permission de sortir de chez soi. Pour des adultes censément libres et autonomes, cette régression au stade de l'enfant qui demande la permission à ses parents était humiliante, mais la plupart ne s'en rendaient même pas compte."""
            },
            {
                "sous_titre": "Le vaccin comme objet sacré",
                "texte": """Quand les vaccins sont arrivés, ils sont devenus immédiatement des objets sacrés, au sens anthropologique du terme. Remettre en question leur efficacité ou leur sécurité n'était pas simplement une opinion différente, c'était un blasphème.

Les personnes qui exprimaient des doutes, même mesurés et argumentés, étaient immédiatement excommuniées du corps social. On ne discutait pas avec elles, on les insultait. Le vocabulaire religieux n'est pas exagéré : c'était bien une réaction de type inquisitorial contre les hérétiques."""
            },
            {
                "sous_titre": "L'échec de la prophétie",
                "texte": """Un phénomène fascinant s'est produit quand les promesses initiales se sont révélées fausses. On nous avait dit que le vaccin empêcherait la transmission, que deux doses suffiraient. Tout cela s'est avéré inexact.

Le psychologue Léon Festinger avait étudié ce phénomène. Quand la prophétie échoue, les adeptes ne se réveillent pas. Au contraire, ils inventent une nouvelle raison de croire et deviennent encore plus fanatiques qu'avant."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 5 : LA DESTRUCTION DE LA MÉMOIRE ET LE PRÉSENTISME",
        "sections": [
            {
                "sous_titre": "L'amnésie comme condition de l'hypnose",
                "texte": """L'hypnose sociale ne peut fonctionner que si elle efface en permanence les traces de ses propres contradictions. Pour que le sujet accepte une nouvelle injonction qui contredit la précédente, il faut qu'il ait oublié la précédente. Cette amnésie n'est pas accidentelle, elle est cultivée, entretenue, systématisée.

Le but est de produire des individus sans racines, sans repères temporels, incapables de mettre en perspective ce qui leur arrive. Des êtres qui vivent dans un présent perpétuel, sans passé pour les éclairer ni futur pour les guider."""
            },
            {
                "sous_titre": "Le présentisme",
                "texte": """L'historien François Hartog a proposé le concept de "régimes d'historicité" pour décrire les différentes manières dont les sociétés se rapportent au temps. Notre époque, selon lui, est caractérisée par le "présentisme" : un présent perpétuel et obèse qui écrase à la fois le passé et le futur.

Dans le présentisme, le passé n'est plus une source de leçons et d'exemples, il est au mieux un exotisme, au pire un repoussoir. Le futur n'existe plus comme projet ou comme espérance, il n'est que menace."""
            },
            {
                "sous_titre": "Le discours du capitaliste",
                "texte": """Cette destruction de la mémoire s'inscrit dans ce que Lacan appelait le "discours du capitaliste". La logique de ce discours est simple : achète ma marchandise et tu ne sentiras plus ton manque. Le manque fondamental de l'être humain devient une faille à combler par la consommation.

Un être qui connaît son histoire, qui est enraciné dans une tradition, est un être qui a des ressources intérieures pour affronter l'existence. Il n'a pas besoin de consommer frénétiquement pour se sentir exister."""
            },
            {
                "sous_titre": "Construire avant de déconstruire",
                "texte": """Une confusion fréquente consiste à croire que le déconstructivisme est toujours une bonne chose. C'est oublier un principe fondamental : on ne peut déconstruire que ce qui a d'abord été construit.

Un enfant qui n'a pas d'abord intégré les mythes de sa culture n'a rien à déconstruire. Il n'accède pas à un niveau supérieur de conscience, il reste simplement dans le vide."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 6 : LA PULSION RÉGRESSIVE ET L'UTÉRUS ARTIFICIEL",
        "sections": [
            {
                "sous_titre": "Le désir de retourner dans le ventre maternel",
                "texte": """Au cœur de la vulnérabilité humaine à l'hypnose sociale se trouve ce qu'on peut appeler la pulsion régressive : le désir profond, souvent inconscient, de retourner dans le ventre maternel. Ce désir est universel car il correspond à une réalité fondamentale de notre développement.

La naissance est le premier traumatisme. Nous sommes expulsés de ce paradis pour être projetés dans un monde froid, bruyant, agressif. Toute notre vie peut être vue comme une série de tentatives pour retrouver cette sécurité perdue."""
            },
            {
                "sous_titre": "L'utérus artificiel du système",
                "texte": """Le système moderne exploite cette pulsion régressive en offrant des substituts à l'utérus maternel. Le divertissement permanent, les réseaux sociaux, les services de livraison à domicile, tout cela crée un cocon artificiel où l'on peut vivre sans affronter véritablement le monde.

Le smartphone est l'utérus portatif parfait. Toujours à portée de main, il offre une stimulation constante, une connexion permanente à une communauté virtuelle."""
            },
            {
                "sous_titre": "L'abolition du fardeau de la liberté",
                "texte": """Erich Fromm, dans "La peur de la liberté", avait analysé ce mécanisme dès les années 1940. Il montrait comment les régimes totalitaires séduisent les masses en leur offrant une prime de plaisir : l'abolition du fardeau de la liberté.

Car la liberté est un fardeau. Être libre signifie être responsable de ses choix, assumer les conséquences de ses actes, affronter l'incertitude. La plupart des gens préfèrent échanger cette liberté contre la sécurité d'un cadre rigide qui leur dit quoi faire."""
            },
            {
                "sous_titre": "La mort du père symbolique",
                "texte": """Pour que la pulsion régressive triomphe complètement, il fallait éliminer ce qui s'y oppose traditionnellement : la fonction paternelle. Le père, dans l'économie psychique, est celui qui arrache l'enfant à la fusion maternelle pour l'introduire dans le monde symbolique et social.

En Occident, cette fonction paternelle a été systématiquement attaquée et démantelée. Nietzsche annonçait que Dieu est mort, et avec lui cette figure du Père universel."""
            },
            {
                "sous_titre": "L'illusion de l'homme providentiel",
                "texte": """Face à l'absence du père symbolique, beaucoup cherchent un substitut dans la figure de l'homme providentiel. C'est une illusion dangereuse. L'homme providentiel est toujours décevant une fois qu'on le connaît de près.

Être adulte, c'est réaliser qu'il n'y a pas de papa. C'est accepter le trou du réel, ce vide fondamental que rien ni personne ne viendra combler. C'est se résigner à générer son propre axe si l'on veut être un individu verticalisé."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 7 : MACRON ET LA PERVERSION AU POUVOIR",
        "sections": [
            {
                "sous_titre": "Un archétype pour l'histoire",
                "texte": """Emmanuel Macron restera une figure archétypale à l'échelle de l'histoire de l'humanité, au même titre que Néron ou Caligula. Non pas nécessairement par l'ampleur de ses crimes, mais par la pureté avec laquelle il incarne certains mécanismes psychologiques du pouvoir pervers.

Ce qui frappe chez Macron, c'est sa capacité à se dénoncer lui-même en permanence. "Je leur ai balancé une grenade dans les genoux", déclare-t-il en parlant de ses adversaires politiques. C'est exactement ce qu'il fait, littéralement."""
            },
            {
                "sous_titre": "Le solve et coagula",
                "texte": """La logique profonde de l'action macronienne peut se résumer par la formule alchimique "solve et coagula" : dissoudre et coaguler. D'abord détruire les liens existants, fragmenter la société en individus isolés. Ensuite recomposer selon un nouveau plan, reconstruire sur les décombres une structure entièrement contrôlée.

Macron lui-même a déclaré : "Il faut d'abord tout détruire pour reconstruire." Cette phrase révèle une philosophie, pas simplement une tactique."""
            },
            {
                "sous_titre": "La stratégie du choc permanent",
                "texte": """Le macronisme repose sur une stratégie du choc permanent qui maintient la population dans un état de sidération propice à l'hypnose. Les crises se succèdent sans répit : Gilets Jaunes, Covid, guerre en Ukraine, inflation, élections anticipées.

L'épuisement de la population est recherché délibérément. Des gens qui travaillent comme des forcenés, bombardés d'informations anxiogènes en permanence, n'ont plus l'énergie de résister ni même de penser."""
            },
            {
                "sous_titre": "L'inversion accusatoire permanente",
                "texte": """Une technique récurrente du macronisme est l'inversion accusatoire : accuser les autres de ce qu'on fait soi-même. Macron accuse ses opposants de vouloir détruire la France alors qu'il la détruit méthodiquement. Il traite de complotistes ceux qui dénoncent ses manipulations.

Cette technique crée la confusion et paralyse l'opposition. Le langage lui-même est colonisé."""
            },
            {
                "sous_titre": "Le flic dans la tête",
                "texte": """La réussite ultime de cette perversion est l'installation du flic dans la tête de chaque citoyen. Non pas un contrôle externe par la force brute, mais une intériorisation du contrôle par le sujet lui-même. C'est ce que Bourdieu appelait la violence symbolique.

Le sujet hypnotisé ne ressent pas le besoin qu'on le surveille car il se surveille lui-même. Il n'a pas besoin qu'on lui dise ce qu'il doit penser car il pense spontanément ce qu'il faut."""
            }
        ]
    },
    {
        "titre": "CHAPITRE 8 : LES COLLECTIFS LIQUIDES ET LA SORTIE DE L'HYPNOSE",
        "sections": [
            {
                "sous_titre": "L'impossibilité des organisations rigides",
                "texte": """Toute organisation qui se rigidifie finit par être capturée par le pouvoir ou par reproduire les pathologies du pouvoir. C'est une loi quasi universelle que l'histoire vérifie à chaque génération.

Ce phénomène n'est pas accidentel, il est structurel. Dès qu'une organisation se dote de structures permanentes, de hiérarchies fixes, de règles immuables, elle crée les conditions de sa propre corruption."""
            },
            {
                "sous_titre": "La solution des collectifs liquides",
                "texte": """Face à cette fatalité de l'institutionnalisation, une piste s'ouvre : celle des collectifs liquides. Un collectif liquide est une forme d'organisation qui ne se rigidifie pas, qui ne crée pas de norme pathologique, qui reste en mouvement permanent.

Les caractéristiques d'un collectif liquide sont : une durée limitée dans le temps, une absence de hiérarchie fixe, une capacité de reconfiguration permanente."""
            },
            {
                "sous_titre": "La redescente vers le cœur",
                "texte": """Au-delà des formes d'organisation, la sortie de l'hypnose passe par un travail intérieur que la tradition décrit souvent comme une "redescente vers le cœur". L'humanité moderne vit dans sa tête, prisonnière de ses pensées, de ses concepts, de ses narratifs.

Le mental est un bon serviteur et un mauvais maître. Quand il est au service du cœur, il est un outil précieux. Quand il prend le pouvoir, il nous enferme dans des transes hypnotiques."""
            },
            {
                "sous_titre": "Le réel lacanien",
                "texte": """Lacan parlait du "réel" comme de ce qui fait irruption dans notre monde symbolique pour nous montrer que notre carte n'est pas le territoire. Le réel est ce qui résiste à nos constructions mentales.

Les arts de combat offrent une expérience régulière du réel. On peut élaborer toutes les théories qu'on veut sur le combat, mais quand on ressort avec un peu de sang sur la bouche, on se rappelle qu'il y a quelque chose qui dépasse nos théories."""
            },
            {
                "sous_titre": "Le travail individuel comme préalable",
                "texte": """Il ne peut pas y avoir de changement extérieur sans nouvelle donne intérieure. C'est une vérité que l'activisme politique refuse généralement d'entendre car elle remet en question sa raison d'être.

Les révolutions qui ne s'accompagnent pas d'une transformation intérieure des révolutionnaires reproduisent les mêmes structures qu'elles prétendaient abolir. Le travail individuel n'est pas un repli égoïste, c'est la condition préalable à toute action collective efficace."""
            }
        ]
    }
]

CONCLUSION = {
    "titre": "CONCLUSION : VERS L'INGÉNIERIE DU CONSENTEMENT",
    "contenu": """Ce document sur la phénoménologie de l'hypnose sociale a posé les bases de la compréhension de notre condition:

1. Nous sommes presque tous en transe la plupart du temps - dissociative ou identificatoire

2. Cette transe est exploitée par les politiciens, publicitaires et ingénieurs sociaux

3. Les mécanismes sont multiples : destruction de la mémoire, pulsion régressive, illusion groupale, identification à l'agresseur

4. Le système se perpétue par substitution (une crise chasse l'autre), par la logique de l'institution, et par l'inversion de la normalité

5. La sortie passe par le travail individuel (pas de changement extérieur sans nouvelle donne intérieure), la redescente du mental vers le cœur, et éventuellement des collectifs liquides

L'hypnomachie est un combat de longue haleine qui ne connaîtra probablement jamais de victoire finale. Mais ce combat n'est pas vain pour autant. Chaque individu qui s'éveille un peu, même temporairement, contribue à affaiblir l'emprise de l'hypnose collective.

La tradition enseigne que les moments d'éveil, aussi brefs soient-ils, ont une valeur inestimable. Ces instants où le voile se déchire, où l'on voit les choses telles qu'elles sont, ces instants changent quelque chose en profondeur.

C'est pourquoi il faut continuer le combat, sans espoir excessif mais sans désespoir non plus. Continuer à chercher l'éveil pour soi-même. Continuer à aider ceux qui le cherchent. Continuer à créer des espaces où la transe a moins de prise."""
}

REFERENCES = """
RÉFÉRENCES CITÉES

Livres
- Howard Bloom, Le Principe de Lucifer (1 et 2)
- Pierre Janet, L'automatisme psychologique (1889)
- Ernest Hilgard, Divided Consciousness (1977)
- Erich Fromm, La peur de la liberté (1941)
- Hannah Arendt, Les origines du totalitarisme
- Noam Chomsky, La fabrique du consentement
- Arthur Koestler, Le zéro et l'infini
- Alexandre Zinoviev, Les hauteurs béantes
- Norbert Elias, La civilisation des mœurs
- François Hartog, Régimes d'historicité
- Milan Kundera, Le livre du rire et de l'oubli (1979)
- Jean Baudrillard, Simulacres et simulation
- Paul Watzlawick, La réalité de la réalité
- Didier Anzieu, Le groupe et l'inconscient (1975)
- Léon Festinger, L'échec d'une prophétie
- Christopher Clark, Les somnambules

Films
- Inception (Christopher Nolan)
- Le complot (sur Popieluszko)
- Munich (Steven Spielberg)
- L'homme irrationnel (Woody Allen)

Concepts
- Mimésis (René Girard)
- Discours du capitaliste (Jacques Lacan)
- Violence symbolique (Pierre Bourdieu)
- Formation de masse (Mattias Desmet)
- Agents de mise en conformité (Howard Bloom)
"""

def create_pdf():
    """Génère le PDF complet"""

    output_path = "/home/user/Bascar/Hypnomachie_Reformulation_Complete.pdf"

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2.5*cm,
        bottomMargin=2.5*cm
    )

    styles = getSampleStyleSheet()

    # Styles personnalisés
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=28,
        spaceAfter=10,
        spaceBefore=50,
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold'
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Title'],
        fontSize=18,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=colors.darkblue,
        fontName='Helvetica-Oblique'
    )

    author_style = ParagraphStyle(
        'Author',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=10,
        alignment=TA_CENTER,
        textColor=colors.grey,
        fontName='Helvetica-Oblique'
    )

    chapter_style = ParagraphStyle(
        'ChapterTitle',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=20,
        spaceBefore=30,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    )

    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=13,
        spaceAfter=12,
        spaceBefore=18,
        textColor=colors.darkblue,
        fontName='Helvetica-Bold',
        alignment=TA_LEFT
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=15,
        fontName='Helvetica'
    )

    preambule_style = ParagraphStyle(
        'Preambule',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=10,
        alignment=TA_JUSTIFY,
        leading=15,
        fontName='Helvetica-Oblique',
        leftIndent=20,
        rightIndent=20
    )

    ref_style = ParagraphStyle(
        'References',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_LEFT,
        leading=13,
        fontName='Helvetica'
    )

    # Construction du document
    story = []

    # Page de titre
    story.append(Spacer(1, 4*cm))
    story.append(Paragraph(TITRE_PRINCIPAL, title_style))
    story.append(Paragraph(SOUS_TITRE, subtitle_style))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph(AUTEUR, author_style))
    story.append(Paragraph(PARTIE, author_style))
    story.append(Spacer(1, 2*cm))

    # Ligne décorative
    story.append(Paragraph("_" * 60, ParagraphStyle('Line', alignment=TA_CENTER, textColor=colors.darkblue)))

    story.append(PageBreak())

    # Table des matières
    toc_title = ParagraphStyle(
        'TOCTitle',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=30,
        textColor=colors.darkblue,
        alignment=TA_CENTER
    )
    story.append(Paragraph("TABLE DES MATIÈRES", toc_title))

    toc_item = ParagraphStyle(
        'TOCItem',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=8,
        leftIndent=20
    )

    story.append(Paragraph("• Préambule", toc_item))
    for i, chap in enumerate(CHAPITRES[1:], 1):  # Skip préambule
        story.append(Paragraph(f"• {chap['titre']}", toc_item))
    story.append(Paragraph("• Conclusion : Vers l'ingénierie du consentement", toc_item))
    story.append(Paragraph("• Références citées", toc_item))

    story.append(PageBreak())

    # Préambule
    story.append(Paragraph("PRÉAMBULE", chapter_style))
    story.append(Paragraph(CHAPITRES[0]["contenu"], preambule_style))
    story.append(Spacer(1, 1*cm))
    story.append(Paragraph("_" * 60, ParagraphStyle('Line', alignment=TA_CENTER, textColor=colors.lightgrey)))
    story.append(PageBreak())

    # Chapitres
    for chapitre in CHAPITRES[1:]:
        story.append(Paragraph(chapitre["titre"], chapter_style))

        if "sections" in chapitre:
            for section in chapitre["sections"]:
                story.append(Paragraph(section["sous_titre"], section_style))

                # Diviser le texte en paragraphes
                paragraphs = section["texte"].strip().split("\n\n")
                for para in paragraphs:
                    if para.strip():
                        story.append(Paragraph(para.strip(), body_style))

        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph("_" * 60, ParagraphStyle('Line', alignment=TA_CENTER, textColor=colors.lightgrey)))
        story.append(PageBreak())

    # Conclusion
    story.append(Paragraph(CONCLUSION["titre"], chapter_style))
    paragraphs = CONCLUSION["contenu"].strip().split("\n\n")
    for para in paragraphs:
        if para.strip():
            story.append(Paragraph(para.strip(), body_style))

    story.append(PageBreak())

    # Références
    story.append(Paragraph("RÉFÉRENCES CITÉES", chapter_style))

    ref_lines = REFERENCES.strip().split("\n")
    for line in ref_lines:
        if line.strip():
            if line.startswith("Livres") or line.startswith("Films") or line.startswith("Concepts"):
                story.append(Spacer(1, 0.3*cm))
                story.append(Paragraph(f"<b>{line}</b>", ref_style))
            elif line.startswith("-"):
                story.append(Paragraph(f"  {line}", ref_style))
            elif line.startswith("RÉFÉRENCES"):
                continue
            else:
                story.append(Paragraph(line, ref_style))

    # Pied de page final
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("_" * 60, ParagraphStyle('Line', alignment=TA_CENTER, textColor=colors.darkblue)))
    story.append(Spacer(1, 0.5*cm))

    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        alignment=TA_CENTER,
        textColor=colors.grey,
        fontName='Helvetica-Oblique'
    )
    story.append(Paragraph("Document généré à partir du transcript de l'entretien Parisiste x Hypnomachie, partie 2.", footer_style))

    # Génération du PDF
    doc.build(story)
    print(f"PDF généré avec succès : {output_path}")
    return output_path

if __name__ == "__main__":
    create_pdf()
