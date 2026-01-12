Unit 5 - Formative Coding Exercise

Refactoring Payment Processing Using the Strategy Pattern

Purpose of the Artefact

The purpose of this artefact was to refactor an existing payment processing implementation that relied on a long conditional chain to select payment behaviour. The original design combined payment selection logic and execution within a single method, resulting in tight coupling and reduced maintainability. This artefact explores how the Strategy Pattern can be applied to address these issues by separating payment algorithms from the processor that coordinates their use.



Object-Oriented Principles and Techniques

This exercise applies key object-oriented principles, particularly encapsulation, polymorphism, and adherence to the Open Closed Principle. A PaymentStrategy abstraction defines a common interface for executing payments through a pay(amount) operation. Concrete strategy classes such as CreditCardPayment, PayPalPayment, and BankTransferPayment implement this interface, each encapsulating the behaviour of a specific payment method.

The PaymentProcessor class is refactored to accept a strategy instance and delegate payment execution to it. As a result, the processor no longer contains conditional logic related to specific payment types and is instead responsible only for orchestration. This separation of responsibilities improves cohesion and allows payment behaviour to vary independently of the processor.


Challenges and Resolutions

The primary challenge addressed in this artefact was the reliance on an extended if and elif chain to determine payment behaviour. This approach violated the Open Closed Principle, as introducing a new payment method required modifying the existing processor logic. It also made testing more complex, since all payment paths were embedded within a single method. This challenge was resolved by introducing the Strategy Pattern, which isolates each payment algorithm within its own class and removes conditional complexity from the processor.


Demonstration of Advanced OOP Concepts

This artefact demonstrates advanced object-oriented design by replacing conditional logic with polymorphic behaviour and by separating algorithmic variation from coordination logic. The resulting design is more maintainable, easier to test, and safer to extend, as new payment methods can be introduced without modifying existing code. This approach reflects real-world payment systems, where providers frequently change and must be enabled or disabled dynamically. If the system were to scale further, strategy selection could be externalised through a registry or dependency injection mechanism to support configuration-driven behaviour.
