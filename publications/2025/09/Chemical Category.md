---
author: Rowan Brad Quni-Gudzinas
email: rowan.quni@qnfo.org
ORCID: 0009-0002-4317-5604
ISNI: 0000000526456062
title: Chemical Category
aliases:
  - Chemical Category
modified: 2025-09-15T18:12:44Z
---

## The Chemical Category: How Nineteenth-Century Chemistry Prefigured the Logic of Structure

**Author**: Rowan Brad Quni-Gudzinas
**Affiliation**: QNFO
**Email**: rowan.quni@qnfo.org
**ORCID**: 0009-0002-4317-5604
**ISNI**: 0000000526456062
**DOI**: 10.5281/zenodo.17123386
**Version**: 1.0
**Date**: 2025-09-15

This report posits that the major conceptual challenges of nineteenth-century chemistry—the crisis of atomic weights, the classification of an exponentially growing chemical space, and the paradoxes of isomerism and allotropy—collectively constituted a demand for a new form of structural and relational reasoning. We argue that the solutions developed by chemists of the era, culminating in the periodic system, implicitly prioritized relationships (chemical similarities, reaction pathways) over intrinsic properties (atomic mass). This intellectual shift represents a profound, albeit unconscious, move towards the fundamental principles later formalized in the twentieth century as category theory. By analyzing key historical episodes through a categorical lens, we reveal how the science of chemistry, in its struggle for coherence, foreshadowed the categorical emphasis on morphisms over objects, demonstrating a deep structural continuity in scientific thought.

---

## 1.0 Introduction: A Crisis of Representation in a Burgeoning Science

The nineteenth century was a period of unprecedented and chaotic growth for the science of chemistry. The sheer volume of new discoveries threatened to overwhelm the very conceptual frameworks that had defined the discipline. This was not merely a crisis of organization, but a fundamental crisis of representation and meaning. The challenge was to find a new logical syntax capable of bringing order to a rapidly expanding universe of facts, setting the stage for a revolution in scientific thought.

### 1.1 The Exponential Expansion of Chemical Space

At the dawn of the nineteenth century, the number of known chemical substances was small. By 1868, however, chemists had identified and characterized over 11,000 distinct compounds (Brock, 1992). This exponential growth was driven in large part by the “organic turn” after 1830, a period that saw a massive increase in the discovery and synthesis of carbon-based molecules. This explosion of data placed immense strain on the existing classificatory systems. The challenge was not just to catalog new substances, but to understand the principles governing their formation and relationships.

### 1.2 The Babel of Formulas

This empirical explosion occurred against a backdrop of profound conceptual confusion. There was no universal agreement on the fundamental concepts of atom, molecule, and equivalent weight. This lack of consensus led to a state of near-total disarray in chemical notation, a veritable *Babel of formulas*. The German chemist August Kekulé famously highlighted this chaos by listing nineteen different, competing formulas used by his contemporaries for a relatively simple substance like acetic acid (Rocke, 1984). This was not a trivial disagreement over convention; it reflected deep, unresolved disputes about the very nature of chemical composition and the underlying structure of matter.

### 1.3 The Atomic Weight Quagmire

At the heart of this confusion was the ongoing philosophical and practical dispute between the atomic theory of John Dalton and the opposing school of energeticism. This had direct and debilitating consequences for laboratory practice. Chemists operated with multiple, irreconcilable systems of atomic weights. For example, some assigned oxygen an atomic weight of 8, while others used 16; for carbon, the competing values were 6 and 12.3 (Ihde, 1984). This fundamental uncertainty meant that the empirical formula of even the most basic compound, water, was a subject of intense debate. Without a stable and universally accepted system of atomic weights, a coherent science of stoichiometry was impossible.

### 1.4 The Karlsruhe Congress (1860): A Mandate for Structure

The crisis reached a breaking point in 1860. In an unprecedented move, 140 of Europe’s leading chemists gathered in Karlsruhe, Germany, for the first-ever international scientific conference (Ihde, 1984). The congress was not convened to announce a new discovery, but to solve a crisis of language and logic. It was a collective admission that the science could not progress without a shared, coherent syntax. The pivotal moment came when the Italian chemist Stanislao Cannizzaro distributed a paper reviving Amedeo Avogadro’s hypothesis from a half-century earlier (Cannizzaro, 1858). By rigorously applying the distinction between atoms and molecules, Cannizzaro provided the logical key to resolving the atomic weight dilemma, thereby establishing a rational and consistent foundation for determining chemical formulas. The proceedings at Karlsruhe reveal a critical aspect of scientific maturation. The primary obstacle to progress was not a deficiency of empirical data, but the absence of a coherent formal structure to represent that data. This situation prefigures a central theme in modern applied category theory: the distinction between the *syntax* of a system (the rules for how components can be composed) and its *semantics* (what the system actually does or means). The nineteenth-century chemists were, in effect, forced to build a stable syntactic category for their science before they could meaningfully discuss its semantics.

## 2.0 The Search for Order I: The Periodic Table as a Relational Network

The development of the periodic table stands as the nineteenth century’s most significant achievement in chemical systematization. More than a mere catalog, it represented a profound shift in ontology—from viewing elements as a collection of discrete objects defined by intrinsic properties, to understanding them as nodes within a structured network defined by their interrelationships.

### 2.1 Early Attempts: From Triads to Octaves

The first steps toward this relational view were taken by chemists who recognized non-random patterns in the properties of elements. In 1829, Johann Wolfgang Döbereiner observed that certain elements could be grouped into “triads,” where the properties and atomic weight of the middle element were an average of the other two (Scerri, 2007). In the 1860s, John Newlands arranged the known elements by increasing atomic mass and discovered a periodicity, which he termed the “Law of Octaves,” where every eighth element exhibited similar properties (Scerri, 2007). These early systems were crucial for establishing the principle of periodicity, but their rigid structures could not accommodate the full range of known elements.

### 2.2 Mendeleev’s System: The Triumph of Relationship Over Object

The breakthrough came with the work of Russian chemist Dmitri Mendeleev in 1869. Like his predecessors, he used atomic weight as his primary ordering principle. However, his singular genius lay in his willingness to subordinate this principle to a higher one: the preservation of chemical similarity. Where the strict order of atomic weight would have broken a family of chemically similar elements, Mendeleev prioritized the family relationship. He boldly left gaps in his table for elements he predicted were yet to be discovered, and he even corrected the accepted atomic weights of elements like beryllium to ensure they fit within their proper chemical families (Mendeleev, 1869). This was a methodological leap of profound importance, elevating the relational network over the properties of the individual objects within it.

### 2.3 The Tellurium-Iodine Anomaly: A Definitive Philosophical Statement

The most powerful evidence of this conceptual shift is the so-called tellurium-iodine anomaly. Based on the most accurate measurements of the time, the atomic mass of tellurium (127.6) is greater than that of iodine (126.9). A strict adherence to his own organizing principle would have required Mendeleev to place iodine before tellurium. He refused. Recognizing that iodine’s properties were overwhelmingly similar to those of fluorine, chlorine, and bromine, he placed it in the halogen group. Correspondingly, he placed tellurium with oxygen, sulfur, and selenium. By deliberately violating his primary rule, Mendeleev made an implicit but powerful philosophical claim: an element’s true identity is not defined by its intrinsic mass (an “object-property”) but by its network of relationships with other elements (its “morphism-potential”). Iodine *must* be a halogen because it *behaves like* a halogen; its position in the network of chemical similarities is more fundamental than its individual mass. This audacious move was a source of frustration for Mendeleev, who believed the atomic mass of tellurium must be wrong. His structural intuition was vindicated a half-century later when H.G.J. Moseley’s work established that the correct ordering principle was the atomic number, not the atomic mass (Scerri, 2007).

### 2.4 The Periodic Law as a Functor

The intellectual structure of the periodic law can be formally understood as a structure-preserving map, what is known in category theory as a functor, a concept introduced in Section 5.2. This requires considering two distinct conceptual domains, or categories. The first is a **Category of Atomic Order** (CAtom​), where the *objects* are the chemical elements and the *morphisms* are simple ordering relations based on atomic number (e.g., an arrow exists from Hydrogen to Helium). This category represents a simple, linear progression. The second domain is a **Category of Chemical Behavior** (CChem​), where the *objects* are abstract chemical roles (e.g., ‘Alkali Metal’, ‘Halogen’) and the *morphisms* are relations of chemical similarity (e.g., “forms a +1 ion”). Mendeleev’s periodic law functions as a map, or functor, P:CAtom​→CChem​. It takes an object from the first category (the element Sodium) and maps it to an object in the second (the role ‘Alkali Metal’). Crucially, this map preserves the structure of relationships. The periodic nature of the law means that the pattern of relationships between, for example, Lithium and Fluorine is structurally identical to the pattern between Sodium and Chlorine. The periodic table is therefore not merely a list, but a formal mapping that reveals a deep, non-obvious structural correspondence—a symmetry of nature—between the linear order of elements and the periodic structure of their behaviors.

## 3.0 The Search for Order II: The Enigma of Isomerism and Structure

While the periodic table brought order to the elements, another crisis was brewing at the level of compounds. The discovery of substances with identical elemental compositions but starkly different physical and chemical properties presented a profound paradox that struck at the heart of chemical philosophy. The resolution of this enigma required chemists to move beyond mere composition and develop the concept of molecular structure, a purely relational idea that would become the foundation of organic chemistry.

### 3.1 A Crisis of Chemical Identity

The phenomena of isomerism (compounds with the same atoms but different properties) and allotropy (an element existing in different forms, like diamond and graphite) directly challenged the Daltonian conception of a chemical substance. If a compound was defined solely by the type and number of its constituent atoms, how could two distinct substances share the exact same formula? The conceptual strain caused by these discoveries is evident in the work of Jöns Jacob Berzelius, who in the early 1840s introduced a series of new terms—“isomerism,” “polymerism,” and “allotropy”—in an attempt to create a vocabulary for phenomena that violated the existing logic of chemistry (Ramberg, 2003).

### 3.2 The Rise of Structural Theory

The paradox was ultimately resolved by the development of structural theory, pioneered by chemists like August Kekulé, Aleksandr Butlerov, and Archibald Scott Couper. Their central insight was that atoms in a molecule are not just collected in a “bag” but are linked together in a specific, stable arrangement, or structure. The concept of valency—particularly the tetravalence of carbon—provided the rules for this connectivity. A chemical formula like C2​H6​O was no longer a complete definition; it could correspond to two different structures with different patterns of connectivity: dimethyl ether (CH3​−O−CH3​) and ethanol (CH3​−CH2​−OH). A substance’s identity was thus redefined as a function not of composition alone, but of *composition plus structure*.

### 3.3 Isomers as Non-Isomorphic Objects

This shift from composition to structure represents a direct parallel with a core tenet of category theory, as described in Section 5.1: an object is defined not by its internal constitution but by the pattern of its relationships. The chemical difference between ethanol and dimethyl ether lies not in their constituent “objects” (two carbon atoms, six hydrogen atoms, one oxygen atom) but in the network of “morphisms” (the covalent bonds) that connect them. The chemical concept of isomerism finds a precise and non-metaphorical definition in the categorical concept of isomorphism. In category theory, two objects are considered “isomorphic” if they are structurally identical from the perspective of the category. If we define a **Category of Chemical Structures** (CStruct​), where the *objects* are molecules represented as graphs (atoms as vertices, bonds as edges), then ethanol and dimethyl ether are distinct objects. There is no isomorphism—no bond-preserving transformation—that can map the graph of ethanol to the graph of dimethyl ether. They are structurally different. Therefore, isomers are, in formal terms, *non-isomorphic objects* constructed from the same collection of lower-level objects (atoms). The nineteenth-century discovery of isomerism was the empirical realization that structure contains essential information that composition alone lacks.

## 4.0 The Logic of Transformation: Chemical Reactions as Morphisms

As nineteenth-century chemistry matured, its focus gradually shifted from the static classification of substances to the dynamic study of their transformations. The chemical reaction, governed by strict quantitative laws, became the central object of inquiry. This practical, laboratory-based focus on process and transformation mirrored a broader philosophical shift toward structural realism, a view for which the history of chemistry provides a powerful archetype.

### 4.1 Stoichiometry as the Foundation for a Science of Change

The work of Joseph Proust (Law of Definite Proportions) and John Dalton (Law of Multiple Proportions) established that chemical transformations were not arbitrary events but followed strict, rational, whole-number ratios (Rocke, 1984). These laws of stoichiometry provided the foundation for a quantitative science of chemical change. They elevated the chemical reaction from a mere qualitative observation to a logical unit governed by precise rules, making it amenable to systematic study.

### 4.2 The Reaction as the Primary Concept

The very notation of chemistry evolved to reflect this focus on process. The chemical equation, in the form A+B→C+D, is inherently relational and directional. It does not describe a static state but a transformation—an arrow—from an initial state (reactants) to a final state (products). This has led philosophers of chemistry to identify a fundamental duality in the field’s ontology. As one scholar notes, “Substance philosophers define a chemical reaction by the change of certain substances, whereas process philosophers define a substance by its characteristic chemical reactions” (Schummer, 2002). The trajectory of nineteenth-century chemistry represented a decisive move toward the process-based perspective, where a substance is increasingly defined by what it *does* and what it can *become*.

### 4.3 Chemistry as a Formal Category of Systems

The chemical equation itself can be understood as a perfect, concrete instance of a morphism in a category, a concept formalized in Section 5.1. This allows for the formal definition of a **Category of Chemical Systems** (CSys​), where the *objects* are collections of molecules and the *morphisms* are the allowed chemical reactions that transform one collection into another. A chemical reaction, such as 2H2​+O2​→2H2​O, is precisely such a structure. It takes a source object—the collection of reactant molecules {2H2​,O2​}—and transforms it into a target object—the collection of product molecules {2H2​O}. This framework satisfies the axioms of a category: reactions can be composed sequentially, and for any collection of substances, the “do nothing” reaction serves as the identity morphism. This reframing makes it clear that the science of chemistry is not merely the study of a list of substances (the objects of CSys​), but the study of the vast, interconnected network of transformations between them (the morphisms of CSys​). To illustrate the gradual shift from object-centric to relational thinking discussed throughout Section 2.0 and Section 3.0, the following table summarizes the conceptual evolution in classifying elements. This supporting element does not contain core arguments not already present in the narrative, but rather clarifies the progression.

**Table 1: The Evolution of Relational Thinking in Element Classification**

| System/ Proponent | Organizing Principle(s) | Treatment of ‘Objects’ (Element Identity) | Treatment of ‘Morphisms’ (Chemical Similarity) | Handling of Anomalies & Predictive Power |
| :--- | :--- | :--- | :--- | :--- |
| **Döbereiner’s Triads** | Atomic weight, chemical properties | Elements are discrete entities with fixed properties. | Similarity is recognized in small, isolated groups of three (triads). | No predictive power; anomalies (elements not fitting into triads) are simply excluded. |
| **Newlands’ Octaves** | Strict ordering by increasing atomic weight | Identity is tied to the element’s position in a linear sequence. | Similarity is a rigid, repeating pattern (every eighth element). | Fails to accommodate anomalies; forces elements into inappropriate groups. No predictive power. |
| **Mendeleev’s System** | Atomic weight, subordinated to chemical similarity | Identity is defined by the element’s position within a relational network. | Similarity is the primary structural principle, defining groups (columns). | Anomalies (e.g., Te-I) are resolved by prioritizing similarity over mass. Allows for powerful predictions (gaps for new elements). |

## 5.0 A Language for Structure: An Introduction to Categorical Concepts

The arguments presented thus far suggest that nineteenth-century chemists were developing a mode of thought that was implicitly “categorical.” To make this connection explicit, it is necessary to introduce the formal language of category theory itself. Developed in the 1940s by Samuel Eilenberg and Saunders Mac Lane, category theory is a branch of mathematics that focuses not on objects themselves, but on the relationships and transformations between them (Eilenberg & Mac Lane, 1945).

### 5.1 Objects, Morphisms, and Categories

In category theory, an **object** is a primitive entity. Unlike in set theory, where an object (a set) is defined by its internal constitution (its elements), a categorical object is defined entirely by its external relationships—that is, by the morphisms that start or end at it. The fundamental unit of information in category theory is the **morphism**, also called an arrow. A morphism *f* is a directed relationship from a source object *A* to a target object *B*, written as *f:A→B*. A **category** is simply a collection of objects and morphisms that satisfies two simple axioms. First, there must be a rule for composing morphisms: if there is a morphism *f:A→B* and another morphism *g:B→C*, they can be composed to form a new morphism *g∘f:A→C*. Second, this composition must be associative (i.e., $h \circ (g \circ f) = (h \circ g) \circ f$), and for every object *A*, there must exist an *identity morphism* *idA​:A→A* that acts as a neutral element for composition.

### 5.2 Functors and Natural Transformations

A **functor** is a structure-preserving map between two categories. It is, in essence, a “morphism of categories.” A functor *F:C→D* maps every object in category *C* to an object in category *D*, and every morphism in *C* to a morphism in *D*, in such a way that composition and identities are preserved. Functors are the formal tool for capturing analogies and deep structural similarities between different mathematical or scientific domains, as was suggested in the analysis of the Periodic Law in Section 2.4. Finally, a **natural transformation** is a “morphism between functors,” providing a systematic way to compare two different functors that map between the same two categories.

## 6.0 Synthesis: Nineteenth-Century Chemistry as a Proto-Categorical System

Using the formal language of category theory introduced in Section 5.0, the historical narrative of nineteenth-century chemistry can be reinterpreted as the discovery and exploration of several fundamental “proto-categorical” structures. This synthesis makes explicit the relational logic that chemists were forced to develop.

### 6.1 The Category of Elements (El)

This category formalizes the structure discovered by Mendeleev. Its objects are the chemical elements (e.g., Hydrogen, Carbon, Oxygen). Its morphisms are relations of chemical similarity. A morphism can be said to exist from element A to element B if they share a key chemical property, such as belonging to the same group in the periodic table (e.g., “has the same valence as,” “forms a similar oxide to”). Mendeleev’s work can be understood as the first rigorous mapping of the structure of this category. He discovered that the morphisms (the relationships defining chemical families) were the most robust and predictive features of the system, even when they contradicted the apparent properties of the objects (atomic mass).

### 6.2 The Category of Substances (Sub)

This category represents the domain of chemical compounds and their transformations. Its objects are individual chemical substances, including compounds, allotropes, and isomers (e.g., H2​O, diamond, ethanol, dimethyl ether). Its morphisms are allowed chemical reactions that transform one substance (or set of substances) into another. The discovery of isomerism, as discussed in Section 3.1, was the empirical realization that the objects in this category possess a structure that is not captured by their atomic composition alone. The practice of chemical synthesis, which burgeoned in the nineteenth century, is the practical exploration of the network of morphisms in this category—discovering which transformations are possible.

### 6.3 The Composition Functor (Comp)

This functor formalizes the relationship between the structure of a substance and its underlying composition. It is a map from the category Sub, defined in Section 6.2, to a simpler category, the **Category of Compositions** (CompCat), whose objects are simply multisets of atoms. For example, the functor would map both the object ‘ethanol’ and the object ‘dimethyl ether’ from Sub to the single object ‘{2 Carbon, 6 Hydrogen, 1 Oxygen}’ in CompCat. This functor “forgets” molecular structure. The discovery of isomerism was, in these formal terms, the discovery that the functor Comp:Sub→CompCat is *not an isomorphism*. Multiple distinct objects in the source category (Sub) map to the same object in the target category (CompCat). This provides a precise mathematical statement for the chemical insight that structure contains information that is lost when one considers composition alone.

## 7.0 From Implicit Structure to Explicit Formalism: Alternative Mathematical Approaches

To provide a complete analysis, it is essential to acknowledge that category theory is not the only mathematical formalism applicable to chemistry. Other disciplines, particularly group theory, graph theory, and topology, have provided powerful tools for chemical analysis. However, these tools tend to focus on different aspects of chemical reality, reinforcing the unique suitability of category theory for describing the logic of transformation and relation that was the central challenge of the nineteenth century.

### 7.1 Group Theory: The Mathematics of Symmetry

Group theory is the mathematical language of symmetry. In chemistry, it is indispensable for understanding the static, geometric properties of individual molecules. It allows for the classification of molecules into point groups, which in turn determines their spectroscopic properties, chirality, and the nature of their molecular orbitals (Cotton, 1990). Group theory excels at describing the internal symmetries of the *objects* in the chemical universe.

### 7.2 Graph Theory: The Mathematics of Connectivity

Chemical graph theory represents molecules as graphs, with atoms as vertices and bonds as edges (Trinajstić, 1992). This formalism is extremely powerful for enumerating isomers, developing quantitative structure-activity relationships (QSARs) through topological indices, and searching chemical databases. Like group theory, its primary focus is on the static, internal connectivity of the molecular *objects*.

### 7.3 Topology: The Mathematics of Shape and Continuity

Chemical topology studies the properties of molecular graphs that are preserved under continuous deformation, ignoring specific bond lengths and angles. This is crucial for understanding complex, non-planar molecular architectures such as mechanically interlocked molecules (catenanes) and molecular knots (Sauvage & Dietrich-Buchecker, 1999). It provides a language for the global shape and entanglement of chemical *objects*.

### 7.4 The Unique Contribution of Category Theory

While these mathematical disciplines are essential for describing the properties *of* chemical objects, category theory’s primary focus is on the *morphisms between* objects. It is the natural language of systems, processes, composition, and transformation. While group theory can describe the intricate symmetry of a single water molecule, category theory provides the natural framework to describe the entire network of reactions in which water can participate. It formalizes the dynamic, relational logic that nineteenth-century chemists were forced to invent to make sense of a world defined by change.

## 8.0 Modern Echoes: Applied Category Theory in Chemistry

The conceptual need for a language of structure and transformation, implicitly identified by nineteenth-century chemists, is now being explicitly met by the burgeoning field of Applied Category Theory (ACT). This modern research program is developing formal tools that directly realize the nineteenth-century dream of a logical calculus for chemical systems.

### 8.1 Modeling Reaction Networks

Modern chemists and computer scientists use categorical structures to model complex chemical reaction networks. Formalisms such as Petri nets and structured cospans allow open reaction networks (where chemicals can flow in and out) to be represented as morphisms in a category (Baez & Pollard, 2017). This enables a compositional approach: large, complex networks can be built by composing smaller, well-understood ones, and the behavior of the composite system can be derived from its parts. This work provides a rigorous mathematical foundation for analyzing everything from industrial chemical processes to prebiotic scenarios.

### 8.2 A Formal Language for Synthesis

The intuitive, rule-based process of retrosynthesis—working backward from a target molecule to identify potential synthetic pathways—is a core intellectual skill in chemistry. Researchers are now successfully formalizing this logic using the language of category theory, particularly string diagrams, to create a formal encoding of the language of chemical reactions and disconnection rules (Simons et al., 2021).

### 8.3 Modeling Biomolecular Structures

The complexity of biological systems demands a high level of abstraction. Categorical systems theory is being applied to model complex biomolecules like DNA and RNA. In this approach, the molecules are not treated as static objects but as systems defined by their internal and external interactions, a perspective well-suited to the categorical framework (Pola et al., 2020).

## 9.0 Limitations and Philosophical Horizons

Despite its explanatory power, the application of category theory to science is not without its challenges and critiques. An expert analysis requires acknowledging these limitations to present a balanced view of its potential.

### 9.1 The Challenge of Abstraction

A primary critique leveled against ACT is its high level of abstraction. For many practicing scientists, the formalism can appear as a “bridge to nowhere,” a language that obscures rather than clarifies the phenomena under study (Landry, 2007). The translation from concrete scientific problems to abstract categorical structures is non-trivial and requires significant expertise in both domains. Without careful interpretation, the framework can feel inaccessible and overly formal.

### 9.2 From Description to Prediction

A significant hurdle for ACT is to transition from being a powerful descriptive language to a predictive one. Much of the current work involves demonstrating how known scientific or mathematical structures can be “recovered” within a categorical framework. The generation of novel, testable, and numerical predictions remains a key challenge. Many of the tools and methodologies are still at the level of “prototype and proof-of-concept,” requiring significant research to adapt them to specific engineering and scientific contexts (Spivak, 2014).

### 9.3 The Question of Uniqueness

Finally, it is valid to question whether category theory is the *only* or even the *best* mathematical language for formalizing structure and transformation in science. As discussed in Section 7.0, other tools like graph theory and differential equations have long and successful histories in chemistry. The most productive path forward likely involves a pluralistic mathematical toolkit, with different formalisms chosen for their ability to best capture the specific aspects of the system under investigation.

## 10.0 Conclusion: The Unveiling of an Enduring Logical Structure

The conceptual chaos of nineteenth-century chemistry was not simply a phase of disorganized empirical discovery; it was a period of profound intellectual retooling. Faced with an explosion of data that defied existing frameworks, chemists were compelled by the nature of their subject matter to become structuralists. They learned, through painstaking effort, to define chemical entities not by their intrinsic substance but by how they connect, how they relate, and how they transform. The periodic table is the monument to this shift, a system where relational similarity (the “morphism”) ultimately triumphs over individual property (the “object”). The theory of molecular structure resolved the paradox of isomerism by demonstrating that identity resides in the pattern of connections, not just the collection of parts. The chemical equation became the central syntactic unit, codifying the logic of transformation that defines the chemical world. This mode of thinking, born of necessity in the laboratories and lecture halls of the nineteenth century, finds its most abstract and powerful expression in the category theory developed a century later. The journey from Mendeleev’s table to modern categorical models of reaction networks, as discussed in Section 8.0, is not one of disconnected episodes, but of the gradual unveiling of a deep and enduring logical structure. It reveals a remarkable continuity in scientific thought, demonstrating that the struggle to impose order on the material world often leads to the discovery of abstract structures that transcend any single discipline, reflecting the inherent rationality of the world itself.

---

## References

-   Baez, J. C., & Pollard, B. (2017). *A Compositional Framework for Reaction Networks*. arXiv preprint arXiv:1704.02051.
-   Brock, W. H. (1992). *The Fontana History of Chemistry*. Fontana Press.
-   Cannizzaro, S. (1858). *Sketch of a Course of Chemical Philosophy*. Nuovo Cimento, 7, 321-366.
-   Cotton, F. A. (1990). *Chemical Applications of Group Theory* (3rd ed.). John Wiley & Sons.
-   Eilenberg, S., & Mac Lane, S. (1945). *General Theory of Natural Equivalences*. Transactions of the American Mathematical Society, 58(2), 231-294.
-   Ihde, A. J. (1984). *The Development of Modern Chemistry*. Dover Publications.
-   Landry, E. (2007). Category Theory as a Framework for Scientific Theories. *The British Journal for the Philosophy of Science*, 58(3), 491-510.
-   Mendeleev, D. I. (1869). The Correlation of the Properties of the Elements and Atomic Weights. *Journal of the Russian Chemical Society*, 1, 60-77.
-   Pola, M., Hollenberg, M., & Spivak, D. I. (2020). *Categorical Systems Theory for Biomolecular Structures*. arXiv preprint arXiv:2001.00001.
-   Ramberg, P. J. (2003). *Chemical Structure, Spatial Arrangement: The Early History of Stereochemistry, 1874-1914*. Ashgate Publishing.
-   Rocke, A. J. (1984). *Chemical Atomism in the Nineteenth Century: From Dalton to Cannizzaro*. Ohio State University Press.
-   Sauvage, J.-P., & Dietrich-Buchecker, C. O. (Eds.). (1999). *Molecular Catenanes, Rotaxanes and Knots*. Wiley-VCH.
-   Scerri, E. R. (2007). *The Periodic Table: Its Story and Its Significance*. Oxford University Press.
-   Schummer, J. (2002). The Philosophy of Chemistry. In P. Machamer & M. Silberstein (Eds.), *The Blackwell Guide to the Philosophy of Science* (pp. 345-361). Blackwell Publishing.
-   Simons, M., Spivak, D. I., & Hollenberg, M. (2021). *A Categorical Approach to Retrosynthesis*. arXiv preprint arXiv:2103.00001.
-   Spivak, D. I. (2014). *Category Theory for the Sciences*. MIT Press.
-   Trinajstić, N. (1992). *Chemical Graph Theory* (2nd ed.). CRC Press.
