using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AlfaCoreDumped.Domain.Entities.InternalUser.UserSolicitation
{
    public class RescissionSolicitation
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        [ForeignKey("CreatorUser")] // Foreign key to reference the User entity
        public Guid CreatorUserId { get; set; }

        [Required]
        [ForeignKey("TargetUser")] // Foreign key to reference the User entity
        public Guid TargetUserId { get; set; }

        public User CreatorUser { get; set; }

        public User TargetUser { get; set; }

        [Required]
        public string Status { get; set; }

        [Required]
        [Range(0, 5)]
        public int Rank { get; set; }

        [Required]
        public string RescissionReason { get; set; }

        public string Description { get; set; }

        public DateTime CreationDate { get; set; }

        public DateTime StartDate { get; set; }

        public DateTime EndDate { get; set; }
    }
}
