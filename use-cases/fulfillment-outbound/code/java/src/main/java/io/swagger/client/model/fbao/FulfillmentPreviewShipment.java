/*
 * Selling Partner APIs for Fulfillment Outbound
 * The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
 *
 * OpenAPI spec version: 2020-07-01
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model.fbao;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.fbao.FulfillmentPreviewItemList;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * Delivery and item information for a shipment in a fulfillment order preview.
 */
@ApiModel(description = "Delivery and item information for a shipment in a fulfillment order preview.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2023-10-17T21:02:37.663-07:00")
public class FulfillmentPreviewShipment {
  @SerializedName("earliestShipDate")
  private String earliestShipDate = null;

  @SerializedName("latestShipDate")
  private String latestShipDate = null;

  @SerializedName("earliestArrivalDate")
  private String earliestArrivalDate = null;

  @SerializedName("latestArrivalDate")
  private String latestArrivalDate = null;

  @SerializedName("shippingNotes")
  private List<String> shippingNotes = null;

  @SerializedName("fulfillmentPreviewItems")
  private FulfillmentPreviewItemList fulfillmentPreviewItems = null;

  public FulfillmentPreviewShipment earliestShipDate(String earliestShipDate) {
    this.earliestShipDate = earliestShipDate;
    return this;
  }

   /**
   * The earliest date that the shipment is expected to be sent from the fulfillment center, in ISO 8601 date time format.
   * @return earliestShipDate
  **/
  @ApiModelProperty(value = "The earliest date that the shipment is expected to be sent from the fulfillment center, in ISO 8601 date time format.")
  public String getEarliestShipDate() {
    return earliestShipDate;
  }

  public void setEarliestShipDate(String earliestShipDate) {
    this.earliestShipDate = earliestShipDate;
  }

  public FulfillmentPreviewShipment latestShipDate(String latestShipDate) {
    this.latestShipDate = latestShipDate;
    return this;
  }

   /**
   * The latest date that the shipment is expected to be sent from the fulfillment center, in ISO 8601 date time format.
   * @return latestShipDate
  **/
  @ApiModelProperty(value = "The latest date that the shipment is expected to be sent from the fulfillment center, in ISO 8601 date time format.")
  public String getLatestShipDate() {
    return latestShipDate;
  }

  public void setLatestShipDate(String latestShipDate) {
    this.latestShipDate = latestShipDate;
  }

  public FulfillmentPreviewShipment earliestArrivalDate(String earliestArrivalDate) {
    this.earliestArrivalDate = earliestArrivalDate;
    return this;
  }

   /**
   * The earliest date that the shipment is expected to arrive at its destination.
   * @return earliestArrivalDate
  **/
  @ApiModelProperty(value = "The earliest date that the shipment is expected to arrive at its destination.")
  public String getEarliestArrivalDate() {
    return earliestArrivalDate;
  }

  public void setEarliestArrivalDate(String earliestArrivalDate) {
    this.earliestArrivalDate = earliestArrivalDate;
  }

  public FulfillmentPreviewShipment latestArrivalDate(String latestArrivalDate) {
    this.latestArrivalDate = latestArrivalDate;
    return this;
  }

   /**
   * The latest date that the shipment is expected to arrive at its destination, in ISO 8601 date time format.
   * @return latestArrivalDate
  **/
  @ApiModelProperty(value = "The latest date that the shipment is expected to arrive at its destination, in ISO 8601 date time format.")
  public String getLatestArrivalDate() {
    return latestArrivalDate;
  }

  public void setLatestArrivalDate(String latestArrivalDate) {
    this.latestArrivalDate = latestArrivalDate;
  }

  public FulfillmentPreviewShipment shippingNotes(List<String> shippingNotes) {
    this.shippingNotes = shippingNotes;
    return this;
  }

  public FulfillmentPreviewShipment addShippingNotesItem(String shippingNotesItem) {
    if (this.shippingNotes == null) {
      this.shippingNotes = new ArrayList<String>();
    }
    this.shippingNotes.add(shippingNotesItem);
    return this;
  }

   /**
   * Provides additional insight into the shipment timeline when exact delivery dates are not able to be precomputed.
   * @return shippingNotes
  **/
  @ApiModelProperty(value = "Provides additional insight into the shipment timeline when exact delivery dates are not able to be precomputed.")
  public List<String> getShippingNotes() {
    return shippingNotes;
  }

  public void setShippingNotes(List<String> shippingNotes) {
    this.shippingNotes = shippingNotes;
  }

  public FulfillmentPreviewShipment fulfillmentPreviewItems(FulfillmentPreviewItemList fulfillmentPreviewItems) {
    this.fulfillmentPreviewItems = fulfillmentPreviewItems;
    return this;
  }

   /**
   * Information about the items in the shipment.
   * @return fulfillmentPreviewItems
  **/
  @ApiModelProperty(required = true, value = "Information about the items in the shipment.")
  public FulfillmentPreviewItemList getFulfillmentPreviewItems() {
    return fulfillmentPreviewItems;
  }

  public void setFulfillmentPreviewItems(FulfillmentPreviewItemList fulfillmentPreviewItems) {
    this.fulfillmentPreviewItems = fulfillmentPreviewItems;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    FulfillmentPreviewShipment fulfillmentPreviewShipment = (FulfillmentPreviewShipment) o;
    return Objects.equals(this.earliestShipDate, fulfillmentPreviewShipment.earliestShipDate) &&
        Objects.equals(this.latestShipDate, fulfillmentPreviewShipment.latestShipDate) &&
        Objects.equals(this.earliestArrivalDate, fulfillmentPreviewShipment.earliestArrivalDate) &&
        Objects.equals(this.latestArrivalDate, fulfillmentPreviewShipment.latestArrivalDate) &&
        Objects.equals(this.shippingNotes, fulfillmentPreviewShipment.shippingNotes) &&
        Objects.equals(this.fulfillmentPreviewItems, fulfillmentPreviewShipment.fulfillmentPreviewItems);
  }

  @Override
  public int hashCode() {
    return Objects.hash(earliestShipDate, latestShipDate, earliestArrivalDate, latestArrivalDate, shippingNotes, fulfillmentPreviewItems);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class FulfillmentPreviewShipment {\n");
    
    sb.append("    earliestShipDate: ").append(toIndentedString(earliestShipDate)).append("\n");
    sb.append("    latestShipDate: ").append(toIndentedString(latestShipDate)).append("\n");
    sb.append("    earliestArrivalDate: ").append(toIndentedString(earliestArrivalDate)).append("\n");
    sb.append("    latestArrivalDate: ").append(toIndentedString(latestArrivalDate)).append("\n");
    sb.append("    shippingNotes: ").append(toIndentedString(shippingNotes)).append("\n");
    sb.append("    fulfillmentPreviewItems: ").append(toIndentedString(fulfillmentPreviewItems)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

