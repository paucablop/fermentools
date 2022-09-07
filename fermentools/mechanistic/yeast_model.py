from kineticmodels.uptake_models import Monod, MonodSubstrateInhibition, MonodSubstrateCompetitiveInhibition, MonodSubstrateNonCompetitiveInhibition


class YeastModel:
    def __init__(
        self,
        model_type: str,
        substrate_biomass_yield: float,
        substrate_product_yield: float,
        **kwargs
    ):
        if model_type == "monod":
            self.model = Monod(**kwargs)
        elif model_type == "monod_substrate_inhibition":
            self.model = MonodSubstrateInhibition(**kwargs)
        elif model_type == "monod_non_competitive":
            self.model = MonodSubstrateNonCompetitiveInhibition(**kwargs)
        elif model_type == "monod_competitive":
            self.model = MonodSubstrateCompetitiveInhibition(**kwargs)
        else:
            raise ValueError("Model type not recognized")
        self.model_type = model_type
        self.substrate_biomass_yield = substrate_biomass_yield
        self.substrate_product_yield = substrate_product_yield

    def calculate_rates(
        self,
        substrate_concentration: float,
        biomass_concentration: float,
    ):
        substrate_rate = - self.model.rate(substrate_concentration) * biomass_concentration
        biomass_rate = - substrate_rate * self.substrate_biomass_yield
        product_rate = - substrate_rate * self.substrate_product_yield


        return [substrate_rate, biomass_rate, product_rate]