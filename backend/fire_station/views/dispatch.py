"""Module for handle dispatch."""
from typing import Any
from django.http import HttpRequest
from django.db.models import QuerySet, Count, Avg, F
from rest_framework import generics, mixins, response, status
from fire_station import models, serializer
from django.utils import dateparse


class DispatchListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    """Return list of dispatches when GET request and create new dispatches when POST request."""

    serializer_class = serializer.DispatchSerializer

    def get_queryset(self) -> QuerySet:
        """Dispatches view return list of all dispatches."""
        return models.Dispatch.objects.all()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by return with list of dispatches.

        :param request: Http request object
        :return: Http response object
        """
        return self.list(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle post request by creating dispatches and return list of dispatches.

        :param request: Http request object
        :return: Http response object
        """
        self.create(request, *args, **kwargs)

        serializer = self.get_serializer(self.get_queryset(), many=True)

        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


class DispatchDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    """Return detail of dispatches when GET request and edit dispatch when PUT request."""

    serializer_class = serializer.DispatchSerializer

    def get_queryset(self) -> QuerySet:
        """Dispatches detail view return list of all dispatches."""
        return models.Dispatch.objects.all()

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by return dispatch detail.

        :param request: Http request object
        :return: Http response object
        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle put request by updating dispatches and return list of all dispatches."""
        self.update(request, partial=True, *args, **kwargs)

        serializer = self.get_serializer(self.get_queryset(), many=True)

        return response.Response(serializer.data, status=status.HTTP_200_OK)


class DispatchAggregate(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView
):
    """Dispatch aggregate view."""

    serializer_class = serializer.DispatchSerializer

    def get_queryset(self) -> QuerySet:
        """Dispatch aggregate view return aggregated dispatches data."""
        queryset = models.Dispatch.objects.all()

        months = self.request.query_params.get("months")
        if months:
            parse_months = months.split(",")
            queryset = queryset.filter(reported_time__month__in=parse_months)

        # 2023-03-15T14:30 example format
        try:
            start_time = dateparse.parse_datetime(self.request.query_params.get("start_time"))
            queryset = queryset.filter(reported_time__gte=start_time)
        except (ValueError, TypeError):
            pass

        try:
            end_time = dateparse.parse_datetime(self.request.query_params.get("end_time"))
            queryset = queryset.filter(reported_time__lte=end_time)
        except (ValueError, TypeError):
            pass

        return queryset

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> response.Response:
        """Handle get request by aggregating dispatches.

        :param request: Http request object
        :return: Http response object
        """
        queryset = self.get_queryset()

        group_by : str = self.request.query_params.get('group_by')  # incident, station, or any valid attributes

        # Dispatch assignments group by "group_by" query param
        if group_by:
            aggregate_data = queryset.values(group_by).annotate(average_time_resolved=Avg(F('notified_time') - F('resolved_time')), number_of_dispatches=Count('id'))

        # All dispatch assignments
        else:
            aggregate_data = queryset.aggregate(average_time_resolved=Avg(F('notified_time') - F('resolved_time')), number_of_dispatches=Count('id'))

        return response.Response(aggregate_data, status=status.HTTP_200_OK)
