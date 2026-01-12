Unit 3 Formative Coding Exercise

Implementing the Factory Method Pattern

Purpose of the Artefact

The purpose of this artefact was to apply the Factory Method Pattern to address common object creation challenges in object-oriented systems, particularly tight coupling between client code and concrete implementations. In the context of a simplified car manufacturing domain, the pattern enables different types of cars to be created without requiring the client to be aware of the specific classes being instantiated. This approach directly mitigates the risk of hardcoded dependencies and supports extensibility by allowing new product types to be introduced with minimal impact on existing logic.



Object-Oriented Principles and Techniques

This artefact applies core object-oriented principles, including abstraction, encapsulation, and polymorphism. An abstract Car class defines a common interface through the drive() method, ensuring that all concrete car implementations adhere to a consistent behavioural contract. Concrete classes such as Sedan, SUV, and Hatchback implement this interface, each providing specialised behaviour while remaining interchangeable from the perspective of the client.

Object creation responsibilities are delegated to an abstract CarFactory class, which defines the factory method create_car(). Concrete factory classes override this method to instantiate specific car types. As a result, the client interacts exclusively with abstractions rather than concrete classes. A simple registry mechanism is used to resolve the appropriate factory based on a type identifier, demonstrating how object creation can be configured dynamically without importing or referencing concrete product classes directly.


Challenges and Resolutions

A key challenge addressed in this exercise was avoiding conditional logic and hardcoded class references for object creation. Such approaches tend to reduce maintainability and violate the Open Closed Principle, as adding new product types requires modification of existing logic. This challenge was resolved by encapsulating object creation within factory classes, thereby isolating change and ensuring that extensions could be introduced through new subclasses rather than modifications to existing code. The use of a registry further reduced coupling by decoupling factory selection from client logic.


Demonstration of Advanced OOP Concepts

This artefact demonstrates advanced object-oriented design by aligning implementation decisions with recognised design principles and best practices. The Factory Method Pattern enables extension without modification, supports loose coupling, and improves maintainability by separating creation logic from usage. These characteristics make the design suitable for larger and evolving systems, such as enterprise manufacturing software where new product variants are introduced regularly. If the system were to scale further, additional enhancements such as automated testing of factory outputs and configuration-driven factory selection could be introduced to improve robustness and flexibility.
