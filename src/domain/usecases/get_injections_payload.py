from domain.interfaces import EnvironmentVariablesController, DependencyInjectionBridge
from domain.models import InjectionsPayload


class GetInjectionsPayload:
    def __init__(
        self,
        environment_variables_controller: EnvironmentVariablesController,
        dependency_injection_bridge: DependencyInjectionBridge,
    ):
        self.environment_variables_controller = environment_variables_controller
        self.dependency_injection_bridge = dependency_injection_bridge

    def call(self) -> InjectionsPayload:
        injections = self.environment_variables_controller.get_injections()
        return self.dependency_injection_bridge.get_injections_payload(injections)