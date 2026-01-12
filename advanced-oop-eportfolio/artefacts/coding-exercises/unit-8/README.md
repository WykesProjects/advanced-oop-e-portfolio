Unit 8  Formative Coding Exercise

Refactoring Pricing Logic Using Constants and the Strategy Pattern

Purpose of the Artefact

The purpose of this artefact was to analyse and refactor an existing pricing function that, while functionally correct, exhibited several maintainability and readability issues. The original implementation relied on hardcoded discount values and conditional logic to apply pricing rules, making the code difficult to extend and reason about. This artefact explores progressive refactoring approaches to improve clarity, maintainability, and adherence to object-oriented design principles.


Object-Oriented Principles and Techniques

This exercise applies object-oriented principles including encapsulation, polymorphism, and the Open Closed Principle. An initial refactoring step replaces magic numbers with named constants, improving readability and reducing duplication while preserving the original structure. A more scalable solution is then introduced using the Strategy Pattern, where each discount rule is encapsulated within its own class implementing a shared interface.

Concrete strategy classes represent individual discount behaviours, and a registry is used to resolve the appropriate strategy based on item type. This approach separates pricing calculation from discount logic, allowing behaviour to vary independently of the pricing loop. By delegating discount application to interchangeable strategy objects, the design supports extension without requiring modification of existing logic.


Challenges and Resolutions

The primary challenges addressed in this artefact were the use of hardcoded values and an extended if and elif chain within a single pricing function. These issues reduced readability, increased the risk of errors during change, and violated the Open Closed Principle by requiring direct modification to support new discount rules. These challenges were resolved through incremental refactoring, first by introducing named constants and then by replacing conditional logic with polymorphic behaviour using the Strategy Pattern. This progression demonstrates how maintainability can be improved without introducing unnecessary complexity prematurely.


Demonstration of Advanced OOP Concepts

This artefact demonstrates advanced object-oriented design by identifying code smells, evaluating alternative refactoring strategies, and applying a design pattern appropriate to the problem domain. The final design supports extensibility, improves testability, and reduces regression risk by isolating discount behaviour within discrete, independently testable components. This approach reflects real-world retail systems, where pricing rules frequently change due to promotions or policy updates. If the system were to scale further, strategy selection could be externalised through configuration and supported by automated validation to ensure consistent pricing behaviour across product categories.
