ALTER TABLE IF EXISTS public.order_table
    ADD CONSTRAINT fk_dim_date_times FOREIGN KEY (date_uuid)
    REFERENCES public.dim_date_times (date_uuid) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;
CREATE INDEX IF NOT EXISTS fki_fk_dim_date_times
    ON public.order_table(date_uuid);