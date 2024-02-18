from domain.models import Injections, InjectionsPayload


class DependencyInjectionBridge:
    def get_injections_payload(self, injections: Injections) -> InjectionsPayload:
        raise NotImplementedError()